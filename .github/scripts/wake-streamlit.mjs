#!/usr/bin/env node
/**
 * Opens the Streamlit app URL and clicks "Yes, get this app back up!" if the app is sleeping.
 * Run from GitHub Actions when the keepalive workflow detects the sleep page.
 * Requires: npx playwright install chromium (or run from playwright container).
 */
import { chromium } from 'playwright';

const APP_URL = process.env.STREAMLIT_APP_URL;
if (!APP_URL) {
  console.error('STREAMLIT_APP_URL not set');
  process.exit(1);
}

let browser;
try {
  browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  await page.goto(APP_URL, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(2000);

  const wakeButton = page.getByRole('button', { name: /get this app back up/i });
  const count = await wakeButton.count();
  if (count > 0) {
    await wakeButton.first().click();
    console.log('Clicked "Get this app back up" – app should be waking.');
    await page.waitForTimeout(10000);
  } else {
    console.log('App was not sleeping (no wake button found).');
  }
} catch (err) {
  console.error(err);
  process.exit(1);
} finally {
  if (browser) await browser.close();
}
