import java.util.Scanner
import scala.collection.mutable.ArrayBuffer
import scala.util.matching.Regex


object Employee_Journal {
    def main(args:Array[String]): Unit = {
        val sc = new Scanner(System.in)

        var check = true

        var empBuf = new ArrayBuffer[Employee]()
        var manBuf = new ArrayBuffer[Employee]()
        while (check) {
            try {
                println("Please Enter an option:")
                println("\t1) Add employee/manager")
                println("\t2) Print all employees")
                println("\t3) Print employees given manager")
                println("\t4) Quit")
                // if this doesn't work...
                var option = sc.nextLine.toInt
                // throw new NumberFormatException("For input string: \"" + sc.nextLine + "\"")

                // To add employee/manager
                if (option == 1) {
                    println("Press 1 for manager, any other for employee")
                    var option2 = sc.nextLine.trim

                    // For manager
                    if (option2 == "1") {
                        var newMan = addEmployee(sc, true)
                        empBuf += newMan
                        manBuf += newMan
                    }
                    // For employee. Must be tied to manager
                    else {
                        var newMan = addEmployee(sc, false)
                        empBuf += newMan

                        var check2 = true
                        while (check2) {
                            println("Enter name of employee manager: ")
                            var name = sc.nextLine.trim()

                            for (i<- 0 to manBuf.size - 1) {
                                if (name == manBuf(i).name) {
                                    // To add to emplyees_Managed
                                    var managed = new ArrayBuffer[Employee]()
                                    if (manBuf(i).employees_Managed != null) {
                                        managed ++= manBuf(i).employees_Managed
                                        managed += newMan
                                        manBuf(i).employees_Managed = managed.toArray
                                    } else {
                                        manBuf(i).employees_Managed = Array(newMan)
                                    }
                                    check2 = false
                                }

                            }
                        }
                    }
                }

                // To print all employees in empBuf
                else if (option == 2) {
                    empBuf.foreach(println)
                }

                // To print employees based on manager
                else if (option == 3) {
                    println("Enter name of manager: ")
                    var name = sc.nextLine().trim
                    for (i <- 0 to manBuf.size - 1) {
                        if (manBuf(i).name == name) {
                            if (manBuf(i).employees_Managed == null) {
                                println("NO EMPLYEES MANAGED")
                            }
                            manBuf(i).employees_Managed.foreach(println)
                        }
                    }
                }

                // To quit
                else if (option == 4) {
                    check = false
                }

                // What happens when user enters a number that is not a 1, 2, 3, or 4
                else {
                    // throw custom exception
                    throw new BadUserInputException()
                }

            } catch {
                case bui:BadUserInputException => {
                    println()
                    println(bui.getMessage())
                    println()
                }
                case nfe:NumberFormatException => {
                    println("Invalid option: Try again!")
                }
                case e:Exception => println("OH NO, EXCEPTION!")
            }
        }
    }

    def addEmployee(sc:Scanner, manCheck:Boolean):Employee = {
        var check = true
        while (check) {
            try {
                println("Enter name of employee: ")
                var name = sc.nextLine.trim()
                val pattern = new Regex("\\W")
                if (pattern.findFirstIn(name) != None) {
                    throw new BadUserInputException
                }
                
                println("Enter age: ")
                var age = sc.nextLine.toInt

                println("Enter department: ")
                var dept = sc.nextLine.trim()

                println("Enter id: ")
                var id = sc.nextLine.toInt

                // For manager
                if (manCheck) {
                    return new Manager(id, name, age, dept)
                }
                // For employee
                else {
                    return new Employee(id, name, age, dept)
                }

            } catch {
                case bui:BadUserInputException => println("NO SPECIAL CHAR IN NAME!!!")
                case e: Exception => println("\n\nINVALID INPUT! TRY AGAIN!\n\n")
            }
        }
        return null
    }
}


// val phoneNumber = new Regex(raw"\(?\d{3}\)?[ -]\d{3}[ -]\d{4}")