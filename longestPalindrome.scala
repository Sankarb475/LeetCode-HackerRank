# solution of https://leetcode.com/problems/longest-palindromic-substring/

import scala.collection.mutable.ArrayBuffer
object Solution  {
    def longestPalindrome(s: String): String = {
        val len = s.length
        if(len == 1 || len ==0) return s
        //var dummy : ArrayBuffer[Char] = ArrayBuffer()
        var palinList : ArrayBuffer[String] = ArrayBuffer()
        for (a <- 0 until len){
          var dummy : ArrayBuffer[Char] = ArrayBuffer(s(a))
          if(palinCheck(dummy) == true){
            palinList.append(dummy.mkString)
            //println(palinList)
          }
            for(b<- a+1 until len){
              dummy.append(s(b))
              if(palinCheck(dummy) == true){
                 palinList.append(dummy.mkString)
              }
            }
        }
        //if(palinList.length == 0) return ""
        return palinList.reduceLeft((x,y) => if (x.length > y.length) x else y)
    }
    def palinCheck(inputString : ArrayBuffer[Char]) : Boolean = {
      val var1 = inputString.mkString
      val var1Rev = var1.reverse
      if (var1 == var1Rev) true 
      else false
      
    }
}



#Another solution 

import scala.annotation._
object OptimizedPalindrome  {
  def longestPalindrome(s: String): String = {
    @tailrec
    def maxAt(startIndex: Int, endIndex: Int): String = {
      if (startIndex < 0 || endIndex > s.length - 1 || s.charAt(startIndex) != s.charAt(endIndex)) 
        s.substring(startIndex + 1, endIndex)
      else 
        maxAt(startIndex - 1, endIndex + 1)
    }
    @tailrec
    def _lp(st: Int, largestYet: String): String = {
      if (st == s.length) largestYet
      else {
        val largestOdd = maxAt(st - 1, st + 1)
        val largestEven = maxAt(st, st + 1)

        if (largestOdd.length > largestEven.length && largestOdd.length > largestYet.length)
          _lp(st + 1, largestOdd)
        else if (largestEven.length > largestOdd.length && largestEven.length > largestYet.length)
          _lp(st + 1, largestEven)
        else
          _lp(st + 1, largestYet)
      }
    }

    _lp(0, "")
  }
}


#Another solution

import scala.collection.mutable.ArrayBuffer
object ShortSolution  {
    def longestPalindrome(s: String): String = {
        val len = s.length
        if(len ==0 || len == 1) return s
        var palinList : ArrayBuffer[String] = ArrayBuffer()
        for (a <- 0 until len){
          var dummy : ArrayBuffer[Char] = ArrayBuffer(s(a))
          palinList.append(s(a).toString.mkString)
            for(b<- a+1 until len){
              dummy.append(s(b))
              val var1 = dummy.mkString
              if(var1 == var1.reverse){
                 palinList.append(dummy.mkString)
              }
            }
        }
        return palinList.distinct.reduceLeft((x,y) => if (x.length > y.length) x else y)
    }
}

val a = ShortSolution.longestPalindrome("jrjnbctoqgzimtoklkxcknwmhiztomaofwwzjnhrijwkgmwwuazcowskjhitejnvtblqyepxispasrgvgzqlvrmvhxusiqqzzibcyhpnruhrgbzsmlsuacwptmzxuewnjzmwxbdzqyvsjzxiecsnkdibudtvthzlizralpaowsbakzconeuwwpsqynaxqmgngzpovauxsqgypinywwtmekzhhlzaeatbzryreuttgwfqmmpeywtvpssznkwhzuqewuqtfuflttjcxrhwexvtxjihunpywerkktbvlsyomkxuwrqqmbmzjbfytdddnkasmdyukawrzrnhdmaefzltddipcrhuchvdcoegamlfifzistnplqabtazunlelslicrkuuhosoyduhootlwsbtxautewkvnvlbtixkmxhngidxecehslqjpcdrtlqswmyghmwlttjecvbueswsixoxmymcepbmuwtzanmvujmalyghzkvtoxynyusbpzpolaplsgrunpfgdbbtvtkahqmmlbxzcfznvhxsiytlsxmmtqiudyjlnbkzvtbqdsknsrknsykqzucevgmmcoanilsyyklpbxqosoquolvytefhvozwtwcrmbnyijbammlzrgalrymyfpysbqpjwzirsfknnyseiujadovngogvptphuyzkrwgjqwdhtvgxnmxuheofplizpxijfytfabx")

