#What we're doing here is making an extension for Markdown
#that will take all the image tags from it and make them work
#with our Photos app.

from django import template
from django.utils.safestring import mark_safe
from xml.etree.ElementTree import *
import markdown

from photo.models import Photo

register = template.Library()

@register.filter('markdown')
def mark(txt):
    html = markdown.markdown(txt, [ImageExtension()])
    print html
    return mark_safe(html)

def processimg(e):
    alt = e.get("alt", "no alt text")
    source = e.get("src")
    try:
        photo = Photo.objects.get(pk=source)
    except:
        print "photo with id %s not found" % source
        return
    title = e.get("title")
    e.tag = "div"
    if not title:
        e.set("class", "inlineImageWrapper")
    else:
        e.set("class", "inlineImageWrapper withCaption")

    content = SubElement(e, 'div')
    content.set("class", "inlineImageContent")

    a = SubElement(content, "a", href=photo.original_image.url)

    #create image
    img = SubElement(a, "img")
    img.set("src", photo.thumbnail.url)
    img.set("alt", alt)

    #create caption if needed
    if not title:
        return

    captionwrapper = SubElement(content, 'div')
    captionwrapper.set("class", "inlinePhotoCaption")
    caption = SubElement(captionwrapper, "span")
    caption.text = title
    

class MyTreeprocessor(markdown.treeprocessors.Treeprocessor):
    def run(self, root):
        for i in root:
            for j in root.getiterator():
                if j.tag == "img":
                   processimg(j)
        return root

class ImageExtension(markdown.Extension):
    def extendMarkdown(self, md, md_globals):
        md.treeprocessors['image'] = MyTreeprocessor()
