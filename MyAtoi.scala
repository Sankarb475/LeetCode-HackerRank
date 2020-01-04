# solution of https://leetcode.com/problems/string-to-integer-atoi/


import scala.math.pow
import scala.util.control.Breaks._
import scala.collection.mutable.ArrayBuffer
import java.lang.NumberFormatException

object AtoiSolution {
    def myAtoi(str: String): Int = {
        val str1 = str.trim
        val arrInt = Array.range(0,10).mkString.toCharArray
        //val arrChar = "abcdefghijklmnopqrstuvwxyz".toCharArray
        if(str1.length ==0) return 0
        
        val b = str.trim.split("\\s+")(0)
        //println(b)
        if(b.length == 1 & !arrInt.contains(b(0).toChar)) return 0
        
        if(b.startsWith("+") || b.startsWith("-") || arrInt.contains(b(0).toChar)) {
          val list = b.toList
          var index = b.length
          //println(index)
          breakable{
            for (i <- 1 until list.length){
              if(!arrInt.contains(list(i).toChar)){
                index = i
                if(index == 1 && list(i).toChar != '.' && (b.startsWith("+") || b.startsWith("-") )) return 0
                break
              }
            }
          }
          //println(b.slice(0,index))
          val d = checkInt(b.slice(0,index))
          return d
        }
        else return 0
    }
    def checkInt(str : String) : Int = {
      //var str1 : String = if(str.length > 12) str.slice(0,12).toString else str.toString
      try{
        val b = str.toLong match{
        case m if m > pow(2,31)-1 => 2147483647
        case m if m < -pow(2,31) => -2147483648
        case other => other
       }
       return b.toInt
      }catch{
        case ex: NumberFormatException =>{
          //println("NumberFormatException")
          var str1 : String = if(str.length > 12) str.slice(0,12).toString else str.toString
          val b = checkInt(str1)
          return b.toInt
        }
      }
    }
}
