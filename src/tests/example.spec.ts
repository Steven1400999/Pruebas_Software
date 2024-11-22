import { test, expect } from '@playwright/test';

//Ingresar con credenciales validas
test('TC_UI_001', async ({page})=> {

  await page.goto('https://www.cyberpuerta.mx/');

  await expect(page).toHaveTitle(/Cyberpuerta.mx: Hardware, Computadoras, Laptops & Más/);

  const ButtonLogIn1 = page.locator("div[id='oxwidget_headerlogin']");
  await expect(ButtonLogIn1).toBeVisible();
  await ButtonLogIn1.click();


  const AccountInput = page.locator("input[id='loginEmail'] ");
  await AccountInput.fill("pruebasdesoftware16854@gmail.com");

  const PasswordInput = page.locator("input[id='loginPasword']");
  await PasswordInput.fill("Root12345.");

  await page.keyboard.press('Enter');


  await expect(page.locator("div[class='oxwidget_headerlogin_title1 large']")).toContainText("Mi cuenta");


}); 

//Ingresar con credenciales invalidas
test('TC_UI_002', async ({page})=> {

  await page.goto('https://www.cyberpuerta.mx/');

  await expect(page).toHaveTitle(/Cyberpuerta.mx: Hardware, Computadoras, Laptops & Más/);

  const ButtonLogIn1 = page.locator("div[id='oxwidget_headerlogin']");
  await expect(ButtonLogIn1).toBeVisible();
  await ButtonLogIn1.click();


  const AccountInput = page.locator("input[id='loginEmail'] ");
  await AccountInput.fill("pruebasdesoftware16854@gmail.com");

  const PasswordInput = page.locator("input[id='loginPasword']");
  await PasswordInput.fill("Root123452.");

  await page.keyboard.press('Enter');


  await expect(page.locator("div[class='error']")).toContainText("¡E-mail ó contraseña errónea!");


});


