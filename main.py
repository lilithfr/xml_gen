import py_xsd._drv as drv
import py_xsd._drv2 as drv2
import py_xsd.binding as xsd

### Some tutorial
###   https://www.liquid-technologies.com/xml-schema-tutorial/xsd-extending-types
###   https://www.codesynthesis.com/projects/xsd/documentation/cxx/tree/manual/#2.11
###   https://stackoverflow.com/questions/39868769/xsd-element-substitution-group-example

class Foo:
    def __init__(self):
        self.male = xsd.gender_t('male')
        self.female = xsd.gender_t('female')
        self.doc = xsd.root()

    def add_default_person(self):
        p = xsd.person_t()
        p.id = 1
        p.age = 32
        p.first_name = "Alex"
        p.last_name = "L"
        p.gender = self.male
        self.doc.person.append(p)

    def add_default_derived(self):
        d = xsd.derived1()
        #d = drv.derived()
        d.extra_text = "Hello World!"
        d.var1 = "my value 1"
        self.doc.item_group.append(d)

    def add_default_derived2(self):
        #d = drv2.derived2()
        d = xsd.derived2()
        d.extra_text = "Hello Universe!"
        d.var3 = "my perfect value 1"
        self.doc.item_group.append(d)

    def gen(self):
        f = open("output.xml", "wb")
        f.write(self.doc.toxml("utf-8", element_name='config'))
        print("done")
        f.close()

def test():
    f = Foo()
    f.add_default_person()
    f.add_default_derived()
    f.add_default_derived2()
    f.gen()

def load():
    rxml = open('xsd/example.xml').read()
    doc = xsd.CreateFromDocument(rxml)
    print("{}".format(doc))

if __name__ == '__main__':
    print("Hello World!")
    test()