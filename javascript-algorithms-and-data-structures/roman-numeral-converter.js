const ROMAN_CONST = [
  ['I', 'V', 'X'],  // for 1-digit number
  ['X', 'L', 'C'],  // for 2-digit number
  ['C', 'D', 'M'],  // for 3-digit number
  ['M']             // for 4-digit number
]

convertToRoman = (num) => {
  str = num + '' 
  let roman = '', ch = ''
  
  for (let i = str.length - 1; i >= 0; i--) {
    ch = str.charAt(str.length - i - 1)

    if (ch === '0') continue
    roman += getRomanNumeral(ROMAN_CONST[i], parseInt(ch))
  }

  return roman
}

getRomanNumeral = (arr, num) => {
        let unitRoman = ''
    
    if (num <= 3) {
        for (let i=0; i < num; i++)
        unitRoman += arr[0]
        
    } else if (num === 4 || num === 9) {
        unitRoman += arr[0]
        unitRoman += (num === 4) ? arr[1] : arr[2]
    
    } else if (num === 5) {
        unitRoman += arr[1]
        
    } else {
        unitRoman += arr[1]
        for (let i=5; i < num; i++)
            unitRoman += arr[0]
    }
    
    return unitRoman
}



