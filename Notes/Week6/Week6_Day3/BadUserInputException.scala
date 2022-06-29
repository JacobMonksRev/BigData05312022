// Custom exception for use in Employee_Journal.scala

class BadUserInputException(message:String) extends Exception(message){
    def this() {
        this("User entered bad data. Please try again!")
    }
}
