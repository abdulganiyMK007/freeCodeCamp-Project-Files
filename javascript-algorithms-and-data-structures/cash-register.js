// Equivalent values of each currency
const CURRENCY_VALUE = [
  ["PENNY", 0.01], 
  ["NICKEL", 0.05],
  ["DIME", 0.1], 
  ["QUARTER", 0.25],
  ["ONE", 1], 
  ["FIVE", 5],
  ["TEN", 10], 
  ["TWENTY", 20],
  ["ONE HUNDRED", 100]
]

// Sum of the all the amount in cash-in-drawer
getSumOfCID = (cid) => {
  let sum = 0
  for (let i = 0; i < cid.length; i++) 
    sum = (sum * 1000 + cid[i][1] * 1000) / 1000
                      
  return sum
}


checkCashRegister = (price, cash, cid) => {
  let change = cash - price
  let changeValues = getInterchange(change, JSON.parse(JSON.stringify(cid)))
  let sum = getSumOfCID(cid)

  if (sum === change) {
    return {status: 'CLOSED', change: cid}

  } else if (change > sum || changeValues[0] != 0) {
    return {status: 'INSUFFICIENT_FUND', change: []}

  } else {
    return {status: 'OPEN', change: changeValues[1]}

  }
}


// 
getInterchange = (change, cid) => {
  let changeDrawer = [], 
  lastIndex = 0, 
  currentUnit = 0
  
  for (let i = CURRENCY_VALUE.length - 1; i >= 0; i--) {
    changeDrawer.push([CURRENCY_VALUE[i][0], 0])
    lastIndex = changeDrawer.length - 1
    currentUnit = CURRENCY_VALUE[i][1]
    
    while (true) {
      // Run while: 
      // amount in current cid > 0
      // change > 0
      // change > the equivalent of current cid
      if (cid[i][1] <= 0 || change <= 0 || change < currentUnit) break 
     
      change = (change*1000 - currentUnit*1000) / 1000
      cid[i][1] = (cid[i][1]*1000 - currentUnit*1000) / 1000
      changeDrawer[lastIndex][1] = (changeDrawer[lastIndex][1]*1000 + currentUnit*1000) / 1000
    }

    
    if (changeDrawer[lastIndex][1] === 0) changeDrawer.pop()
    if (change <= 0) break 
  }
 
  return [change, changeDrawer]

}

