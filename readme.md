XSD Python Example
==================


Branch availables
-----------------

* simple_extension
    Use extension and xsi:type
    
Example of XML output
```xml
<?xml version="1.0" encoding="utf-8"?>
<config xmlns:ns1="http://NamespaceTest.com/DerivedTypes" xmlns:ns2="http://NamespaceTest.com/Derived2Types"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    <person id="1">
        <first-name>Alex</first-name>
        <last-name>L</last-name>
        <gender>male</gender>
        <age>32</age>
    </person>
    <item extra-text="Hello World!" xsi:type="ns1:derived">
        <ns1:var1>my value 1</ns1:var1>
    </item>
    <item extra-text="Hello Universe!" xsi:type="ns2:derived2">
        <ns2:var3>my perfect value 1</ns2:var3>
    </item>
</config>
```

* substitution_group

```xml
<?xml version="1.0" encoding="utf-8"?>
<config xmlns:ns1="http://NamespaceTest.com/DerivedTypes" xmlns:ns2="http://NamespaceTest.com/Derived2Types">
    <person id="1">
        <first-name>Alex</first-name>
        <last-name>L</last-name>
        <gender>male</gender>
        <age>32</age>
    </person>
    <derived1 extra-text="Hello World!">
        <ns1:var1>my value 1</ns1:var1>
    </derived1>
    <derived2 extra-text="Hello Universe!">
        <ns2:var3>my perfect value 1</ns2:var3>
    </derived2>
</config>
```

* substitution_group_multi_xsd

```xml
<?xml version="1.0" encoding="utf-8"?>
<config xmlns:ns1="http://NamespaceTest.com/DerivedTypes" xmlns:ns2="http://NamespaceTest.com/Derived2Types">
    <person id="1">
        <first-name>Alex</first-name>
        <last-name>L</last-name>
        <gender>male</gender>
        <age>32</age>
    </person>
    <ns1:derived1 extra-text="Hello World!">
        <ns1:var1>my value 1</ns1:var1>
    </ns1:derived1>
    <ns2:derived2 extra-text="Hello Universe!">
        <ns2:var3>my perfect value 1</ns2:var3>
    </ns2:derived2>
</config>
```