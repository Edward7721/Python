test.js
/*************************** 
TASK 1: 
Write an automated functional test that ensures that on dokkio.com, 
the QA Engineer job listing is not displayed until you click the “QA Engineer” button.
 Node.js preferred. 
*****************************/ 

var webdriver = require('selenium-webdriver');
var assert = require('assert');
 
var driver = new webdriver.Builder().
   withCapabilities(webdriver.Capabilities.chrome()).
   build(); 

until = webdriver.until,
By = webdriver.By;

/*** this function returns in callback true if QA Job Content displayed, false if not**/
function isJobContentDisplayed(helper){
	driver.wait(until.elementLocated(By.id('Jobs-2-content')), 10000, 'Could not locate element ');
	driver.findElement(By.id('Jobs-2-content')).getAttribute("class").then(function(text) {
    res = (text.indexOf('iw-so-tabs-panel iw-so-tab-active') !=-1);
	helper(res);    
	});
}//isJobContentDisplayed()
 
function clickQAEngineer(){
	//driver.wait(until.elementLocated(By.linkText('#Jobs-2-content')), 10000, 'Could not locate element ').then(
	driver.wait(until.elementLocated(By.xpath("//a[contains(@href,'Jobs-2-content')]")), 10000, 'Could not locate element ').then(
	function(){
	driver.findElement(By.xpath("//a[contains(@href,'Jobs-2-content')]")).click();
	});
}//clickQAEngineer
 
console.log("TEST 1: open Dokkio url, verify QA job content does not displayed");
driver.get('http://www.dokkio.com');
var res=false;
isJobContentDisplayed(function(result){
   	var temp = assert.equal(result,false);
});
console.log("TEST 2: click on 'QA Engineer' job,  verify QA Engineer content is displayed");
clickQAEngineer()
var res=false;
isJobContentDisplayed(function(result){
    var temp = assert.equal(result,true);
}); 
//console.log("TEST 3: click on 'Senior Full Stack Engineer' job,  verify QA Engineer content NOT displayed" //TODO
