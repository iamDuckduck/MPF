let mutual_fund = 41853;

// Annual growth rate
const growthRate = 1.08;

const target = 179990; // need 179990 money for the car

//start calculation from 2040
const saved_variable_expense = 83400 * 0.3 + 4800;

const adjusted_rate_before_postgrad = 1.015; //(0.05 - 0.035)

const adjusted_rate_after_postgrad = 1.065; //(0.01 - 0.035)

const saved_money_from_renting = 60000;

// Initial fund amount
let fund = 41853;

let year = 0;
while (fund < target) {
  year++;
  let cashSurplus = calculateCashSurplus(year);
  fund = (fund + cashSurplus) * growthRate;
}

console.log(` the fund now has ${fund}.`);
console.log(
  `It will take ${year} years to reach the target value of ${target}.`
);

// Annual cash surplus calculation formula
function calculateCashSurplus(year) {
  const cashSurplus =
    saved_variable_expense *
      Math.pow(adjusted_rate_before_postgrad, 7) *
      Math.pow(adjusted_rate_after_postgrad, 7 + year) +
    60000 * Math.pow(adjusted_rate_after_postgrad, year) -
    983.9 * 12 -
    9335 * 12;
  console.log(cashSurplus);
  return cashSurplus < 0 ? 0 : cashSurplus;
}
