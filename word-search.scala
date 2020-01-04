# Solution of https://leetcode.com/problems/word-search/


object WordSearch {
  def exist(board: Array[Array[Char]], word: String): Boolean = {
    for (i <- 0 until board.length){
      for (j <- 0 until board(0).length){
        if(search(board,word,i,j,0)){
          return true
        }
      }
    }
    return false
  }
  
  def search(board : Array[Array[Char]],word : String,i : Int,j: Int,idx: Int) : Boolean = {
    if(idx == word.length) return true
    if ((0 <=i && i<board.length) && (0<=j && j<board(0).length) && board(i)(j) == word(idx)){
      var temp = board(i)(j)
      board(i)(j) = '0'
      var direction = List(List(1,0),List(-1,0),List(0,1),List(0,-1))
      for(m <- 0 until direction.length){
         if(search(board,word,i+direction(m)(0),j+direction(m)(1),idx+1) == true) return true
      }
      board(i)(j) = temp
    }
    return false
  }
}
