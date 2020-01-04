#solution of https://leetcode.com/problems/longest-substring-without-repeating-characters/

import scala.util.control.Breaks._
import scala.collection.mutable.ArrayBuffer
import scala.collection.mutable.Map

object Solution {
    def lengthOfLongestSubstring(s: String) : Int = {
        //var dict : Map[String, Int] = Map()
        var outputArr : ArrayBuffer[Int] = ArrayBuffer()
        val len = s.length
        if(len ==0) return 0
        if (len == 1) return 1
        //println(len)
        for(a <- 0 until len){
            var newS = ArrayBuffer(s(a))
            //println(s"newS = $newS , a = $a ")
            breakable{
               if(a ==len - 1) {
               //println(s"inside $outputArr")
               outputArr.append(1)
               //println(s"inside $outputArr")
               break  
               }
            }
            breakable{
                for(b <- a+1 until len by 1){
                    if(newS.contains(s(b))){
                         //dict += newS.mkString  -> newS.length
                         outputArr.append((newS.mkString).length)
                         //println(outputArr)
                         newS = ArrayBuffer()
                         break
                    } 
                    else
                         //println("I am here")
                         newS.append(s(b))
                         //print(newS)
                         if(b == len - 1){
                            outputArr.append((newS.mkString).length)
                            //println(s"Important $outputArr")
                         }
                }
            }
        }
        //print(outputArr)
        //val output = dict.valuesIterator.max
        val output = outputArr.max
        return output
    }
}
