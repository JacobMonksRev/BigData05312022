object HelloWorld {
    def num1(): Unit = {
        import scala.io.StdIn.readInt
        println("Enter an integer: ")
        var mynum = readInt()
        for (i <- 0 to mynum-1) {
            println(i)
        }
    }
    def num2(): (Int, Int, Int, Float) = {
        import scala.io.StdIn.readInt
        println("Please enter two numbers: ")
        var a = readInt()
        var b = readInt()
        return(a+b, a-b, a*b, a.toFloat/b.toFloat)
    }
    def num3(): String = {
        import scala.io.StdIn.readInt
        println("Please enter two numbers: ")
        var a = readInt()
        var b = readInt()
        return (a/b).toString + "R" + (a%b).toString
    }
    def num4(s1:Set[Any], s2:Set[Any]): (Set[Any], Set[Any]) = {
        return (s1.&(s2), s1.--(s2))
    }
    def num5(a:String): Unit = {
        for (i <- 0 to a.length-1) {
            println(a(i))
        }
    }
    def num6(): Unit = {
        import scala.io.StdIn.readLine
        var name = readLine("Enter your name: ")
        var age = readLine("Enter your age: ")
        var DoB = readLine("Enter your date of birth: ")
        var job = readLine("Enter your job: ")
        var employer = readLine("Enter your employer: ")
        val myMap = Map("Name"->name,"Age"->age,"DoB"->DoB,"Job"->job,"Company"->employer)
        println(myMap)
    }
    def num7(a:Int): Unit = {
        if (a > 10) {
            println("Your number is greater than 10.")
        } else if (a < 10) {
            println("Your number is less than 10.")
        } else println("Your number is 10.")
    }
    def main(args:Array[String]): Unit = {
        println("Hello World!")
        //num1()
        //println(num2())
        //println(num3())
        //println(num4(Set(1,2,3,4,5), Set(3,4,5,6,7)))
        //num5("Jacob")
        //num6()
        num7(56)
    }
}