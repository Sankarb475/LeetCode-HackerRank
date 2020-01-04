

import scala.util.control.Breaks._
import scala.collection.mutable.ArrayBuffer

class SolutionNQueen{
  case class Position(row : Int, col : Int)
  //var col : Int = 0
  //var row : Int = 0
  
  /*trait dummy {
    val positions : ArrayBuffer[Position]
  }
  */
  
  def solveNQueenSolution(n:Int) : ArrayBuffer[Position] = {
    println("Inside solveNQueenSolution")
      var positions = new ArrayBuffer[Position]
      val hasSolution : Boolean = solveProblem(n,0,positions)
      if (hasSolution==true) 
        return positions 
      else 
        return new ArrayBuffer[Position](0)
    
  }
  
  def solveProblem(n: Int, row : Int, positions : ArrayBuffer[Position]) : Boolean={
     if(n == row) return true
     println(s"Inside solveProblem $row")
     breakable{
       for (col <-0 until n by 1) {
         var foundSafe : Boolean = true
         for(queen <-0 until row by 1){
           if (positions(queen).col == col || positions(queen).row - positions(queen).col == row - col
               || positions(queen).row + positions(queen).col == row + col){
             foundSafe = false
             println(s"Inside queen $col , $queen")
             break
           }
           
         }  
         
         if(foundSafe) {
           positions.append(Position(row,col));
           println(positions)
           println(s"Inside solveProblem $row , $col")
           if(solveProblem(n,row + 1,positions))
             return true
         }
       }
     }
     return false
     
  }
  
  
}
