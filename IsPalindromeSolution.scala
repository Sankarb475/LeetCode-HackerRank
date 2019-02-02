object IsPalindromeSolution {
    def isPalindrome(x: Int): Boolean = {
        if (x < 0) return false
        if(x.toString.reverse.toLong == x) return true
        return false
    }
}
