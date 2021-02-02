isPalindrome = (str) => {
    for (let i = 0; i < str.length / 2; i++) 
        if (str.charAt(i) != str.charAt(str.length - i - 1)) 
            return false
  
    return true
}


palindrome = (text) => {
    var filterText = '', aChar = ''
     
    for (let i = 0; i < text.length; i++) {
        aChar = text.charAt(i)

        if (!/(\d|[a-zA-Z])/.test(aChar)) continue
        filterText += (/\d/.test(aChar)) ? aChar : aChar.toLowerCase()
    }

    return isPalindrome(filterText)
}
