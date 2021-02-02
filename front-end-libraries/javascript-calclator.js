import React from 'react';
import ReactDOM from 'react-dom';
//import { Button } from 'react-bootstrap';
import './calculator.css'

const dataNums = [
  {id : 'zero', num : 0},
  {id : 'one', num : 1},
  {id : 'two', num : 2},
  {id : 'three', num : 3},
  {id : 'four', num : 4},
  {id : 'five', num : 5},
  {id : 'six', num : 6},
  {id : 'seven', num : 7},
  {id : 'eight', num : 8},
  {id : 'nine', num : 9},
]

const isSymbol = (param) => /[/*+-]/.test(param)

const dataOps = [
  {id : 'divide', symbol : '/'},
  {id : 'multiply', symbol : '*'},
  {id : 'add', symbol : '+'},
  {id : 'subtract', symbol : '-'},
]



class CalculatorApp extends React.Component {
  constructor(props) {
    super(props)

    this.state = {
      result : '0',
      allInput : '',
      resultChecked : false
    }

    this.handleClick = this.handleClick.bind(this)
    this.handleClear = this.handleClear.bind(this)
    this.handleResult = this.handleResult.bind(this)
  }

  handleClear(e) {
    this.setState({
      result : '0',
      allInput : '',
      resultChecked : false
    })
  }

  handleResult(e) {
    const {innerText} = e.target
    const {allInput} = this.state
    let evalued = eval(allInput)

    if (evalued === undefined) evalued = 0

    let strEvalued = evalued + ''
    if (strEvalued.includes('.') && strEvalued.length - strEvalued.indexOf('.') > 4)
    evalued = evalued.toFixed(4)

    //if (evalued.endsWith('.0000'))

    this.setState({
      result : evalued,
      allInput : allInput + innerText + evalued,
      resultChecked : true
    })

  }


  handleClick(e) {
    const {innerText} = e.target
    const {allInput, result, resultChecked} = this.state

    
    if (resultChecked) {
      if (isSymbol(innerText)) {
        this.setState({
          allInput : result + innerText,
          resultChecked : false,
          result : innerText
        })
        
      } else {
        this.setState({
          allInput : innerText,
          resultChecked : false,
          result : innerText
        })
      }

    } else if (isSymbol(innerText)) {
      let lastChar = allInput.charAt(allInput.length-1)

      if (!isSymbol(lastChar)) {
        this.setState({
          allInput : allInput + innerText,
          result : innerText
        })

      } else if (innerText === '-') {
        if (lastChar === '-') {
          this.setState({
            allInput : allInput.slice(0, allInput.length-1) + '+',
            result : innerText
          })
        } else {
          this.setState({
            allInput : allInput + innerText,
            result : innerText
          })
        }
      
      } else {
        this.setState({
          allInput : allInput.slice(0, allInput.length-1) + innerText,
          result : innerText
        })
      }

    } else if (innerText === '.') {
      if (!allInput.endsWith('.'))

        for (var i=allInput.length-1; i >= 0; i--)
          if (Number.isNaN(Number(allInput.charAt(i))))
            break

        if (!allInput.slice(i).includes('.')) {
          this.setState({
            allInput : allInput + innerText,
            result : innerText
          })
        }  

    } else {
      this.setState({
        allInput : allInput + innerText,
        result : innerText
      })
    }
    
    


    

  }

  render() {
    
    const {allInput, result} = this.state

    return (

      <div className="grid-container">
        <div id='display'>
          <div class='show-inputs'>{allInput}</div>
          <div class='show-result'>{result}</div>
        </div>

        <Pad id='clear' text='AC' click={this.handleClear} />

        {dataNums.map((aValue, index) => {
          return <Pad id={aValue.id} text={aValue.num} click={this.handleClick} />
        })}

        {dataOps.map((aValue, index) => {
          return <Pad id={aValue.id} text={aValue.symbol} click={this.handleClick} />
        })}

        <Pad id='decimal' text='.' click={this.handleClick} />
        <Pad id='equals' text='=' click={this.handleResult} />
        
      </div>
    )
  }
}


function Pad(props) {
  const {id, text, click} = props
  return (
    <button id={id} onClick={click} >{text}</button>
  )
}

ReactDOM.render(<CalculatorApp />, document.getElementById('root'))


export default CalculatorApp;
