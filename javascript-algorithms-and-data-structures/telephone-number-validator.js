/* This matches valid number formats without parenthesis
 * ===============================================================
 * [1 and 0+ space](optional)   555     (  555    or  space\555\space    or      -555-  )   5555
 *      ^(1\s+)?                \d{3}   ((\d{3})  |   (\s+\d{3}\s+)      |     (-\d{3}-))  \d{4}$
 */
let parenthesePattern = /^(1\s+)?\d{3}((\d{3})|(\s+\d{3}\s+)|(-\d{3}-))\d{4}$/


/* This matches valid number formats with parenthesis
 * ===============================================================
 *  (     555    )  [space, 0 or more](optional)    555  -   5555 
 * \(   \d{3}   \)             (\s*)?              \d{3} -  \d{4}$
 */
let noParenthesePattern = /^\(\d{3}\)(\s*)?\d{3}-\d{4}$/


telephoneCheck = (str) => {
    return (str.indexOf(')') === -1) ? parenthesePattern.test(str) : noParenthesePattern.test(str)
}
