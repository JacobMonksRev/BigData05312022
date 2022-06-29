/*
Pillars of OOP

Abstraction
    - Hiding implementation of behavior

Polymorphism
    - Child class can contain same fields and behavior as parent class, but act differently
    - "Many Forms"
    - Method Overriding
    - Method Overloading

Inheritance
    - Child class inherits data fields(attributes) and behavior(menthods) of parent class

Encapsulation
    - Encapsulates data fields (attributes)
    - Make attributes private, accessible through getter/setter methods

*/

// extends Any
class Employee(var id:Int, var name:String, var age:Int, var dept:String) {
    var employees_Managed:Array[Employee] = null

    def this(name:String) = {
        this(-1, name, -1, "NA")
    }

    def inc_Age():Unit = {
        this.age += 1
    }

    def greet():Unit = {
        println("Hello, manager!")
    }

    override def toString():String = {
        var retString = ""
        retString += "id:   " + id + "\n"
        retString += "name: " + name + "\n"
        retString += "age:  " + age + "\n"
        retString += "dept: " + dept + "\n"

        return retString
    }
}

class Manager(id:Int, name:String, age:Int, dept:String)
    extends Employee(id, name, age, dept) {


    override def greet():Unit = {
        println("Hello, employees!")
    }

    def set_Managed(arr:Array[Employee]):Unit = {
        employees_Managed = arr
    }

    
}
