```py
from lxml import etree
# DOC https://lxml.de/api/lxml.etree._Element-class.html

div.getchildren() -> list
div.getparent() -> etree.Element
div.getprevious() -> etree.Element
div.getnext() -> etree.Element
div.getiterator(tag, *tags) -> depth first pre-order
div.find()
div.findall('br'|'*/br'|'*/*/br'|'*//br') # 子节点的 br, 子子节点的 br, 子子子节点的 br, 子子节点之下的所有 br
div.iter()

div.insert(0, etree.Element('p'))
etree.SubElement(div, 'p') == div.append(etree.Element('p'))
div.addprevious(etree.Element('a'))
div.addnext(etree.Element('a'))
div.extend([etree.Element('a'), etree.Element('b'),etree.Element('c')])

div.index(div.find('a'), start=1, end=6) == 5
div.insert(5, etree.Element('a_before'))

# 删除某个节点
for node in dom.xpath('//div[@class="attribution"]'):
    node.getparent().remove(node)

# 高亮小标题
for span in dom.xpath('//h1/span | //h2/span | //h3/span'):
    span_parent = span.getparent()
    span_parent.text = span.text
    span_parent.remove(span)

# 删除属性
for img in dom.xpath('//img'):
    try:
        del img.attrib['srcset']
    except KeyError:
        continue

# 标点错误, ul>li>ul --> ul>ul
for out_ul in dom.xpath('//div/ul'):
    children = out_ul.getchildren()
    if children and all([i.tag == 'li' for i in children]):
        for inner_ul in out_ul.xpath('./li/ul'):
            li = inner_ul.xpath('./li')[0]
            ul = deepcopy(li.getchildren()[0])
            inner_ul.clear()
            inner_ul.append(ul)
```