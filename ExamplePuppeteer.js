const puppeteer = require('puppeteer');


 async function getHistoricGlobalMarketData () {

    // set up puppeteer browser
    console.debug("Loading puppeteer...")
    let browser = await puppeteer.launch({
      headless: process.env.PRODUCTION == "true"
    });
    let page = await browser.newPage();
    await page.setViewport({ width: 700, height: 1200});
    await page.goto('https://coinmarketcap.com/es/charts/');

    page.on('response', async (response) => {
        if (response.url().includes("quotes/historical")){
            console.log('XHR response received');
            console.log(await response.json());
        }
    });
}

if (module === require.main) {
    getHistoricGlobalMarketData()
}

module.exports = {

    getHistoricGlobalMarketData
}