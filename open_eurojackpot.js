const { chromium } = require('@playwright/test');

(async () => {
  // Launch browser
  const browser = await chromium.launch({ headless: false }); // set to true if you don't want to see the browser
  const context = await browser.newContext();
  const page = await context.newPage();

  // Go to Eurojackpot
  await page.goto('https://www.eurojackpot.com/', {
    waitUntil: 'load', // or 'networkidle'
    timeout: 60000
  });

  // Optional: wait a bit so you can see the page
  await page.waitForTimeout(5000);

  // Close browser
  await browser.close();
})();