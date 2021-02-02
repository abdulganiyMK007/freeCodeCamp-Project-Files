const A_CODE = 'A'.charCodeAt()
const Z_CODE = 'Z'.charCodeAt()
const KEY = 13


rot13 = (cypherText) => {

    let decodedText = '', aChar = ''
    for (let i = 0; i < cypherText.length; i++) {
        aChar = cypherText.charAt(i)
        decodedText += (/[\w]/.test(aChar) && aChar != '_') 
            ? decode(aChar.toUpperCase().charCodeAt(0)) : aChar
    }

    return decodedText;
}

decode = (aCode) => {
    let newCode = aCode + KEY
    while (newCode > Z_CODE) newCode += (A_CODE - Z_CODE - 1)

    return String.fromCharCode(newCode)
}
