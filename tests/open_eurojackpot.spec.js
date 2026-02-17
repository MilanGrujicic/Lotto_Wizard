const { test, expect } = require('@playwright/test')

test('read numbers from a eurojackpot', async ({ page }) => {
  await page.goto('https://www.eurojackpot.com/');

  // Change this selector to whatever contains your number
  const numbers = await page.locator('.winning-number').allInnerTexts();

  console.log('Extracted numbers:', numbers);

  const parsedNumbers = numbers.map(n => parseInt(n, 10));
  console.log('Parsed numbers:', parsedNumbers);

  // Assert array lenght
  expect(parsedNumbers.length).toBe(7);
  // Assert all elements are numbers
  for (const n of parsedNumbers) {
    expect(typeof n).toBe("number");
  }
  // Assert numbers are within expected range (1-50 for main numbers, 1-10 for euro numbers)
  for (const n of parsedNumbers.slice(0, 5)) {
    expect(n).toBeGreaterThanOrEqual(1);
    expect(n).toBeLessThanOrEqual(50);
  }
  for (const n of parsedNumbers.slice(5, 7)) {
  expect(n).toBeGreaterThanOrEqual(1);
    expect(n).toBeLessThanOrEqual(10);
  }
  const fs = require('fs');
  fs.writeFileSync('numbers.json', JSON.stringify(parsedNumbers));
}
);