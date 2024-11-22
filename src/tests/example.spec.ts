import { test, expect } from '@playwright/test';

//Ingresar con credenciales validas
test('TC_UI_001', async ({ page }) => {

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

//Ingresar con correo electronico invalido invalidas
test('TC_UI_002', async ({ page }) => {

  await page.goto('https://www.cyberpuerta.mx/');

  await expect(page).toHaveTitle(/Cyberpuerta.mx: Hardware, Computadoras, Laptops & Más/);

  const ButtonLogIn1 = page.locator("div[id='oxwidget_headerlogin']");
  await expect(ButtonLogIn1).toBeVisible();
  await ButtonLogIn1.click();


  const AccountInput = page.locator("input[id='loginEmail'] ");
  await AccountInput.fill("ppruebasdesoftware16854@gmail.com");

  const PasswordInput = page.locator("input[id='loginPasword']");
  await PasswordInput.fill("Root12345.");

  await page.keyboard.press('Enter');

  await expect(page.locator("div[class='error']")).toContainText("¡E-mail ó contraseña errónea!");
});


//Verificar que la barra de busqueda funcione
test('TC_UI_003', async ({ page }) => {

  await page.goto('https://www.cyberpuerta.mx/');
  await expect(page).toHaveTitle(/Cyberpuerta.mx: Hardware, Computadoras, Laptops & Más/);

  const InputArticle = page.locator("input[name='searchparam'][placeholder='¿Qué producto buscas el día de hoy?']");
  await expect(InputArticle).toBeVisible();
  await InputArticle.fill("Audífonos");
  await page.keyboard.press('Enter');

  await expect(page.locator("a[title='Audífonos']")).toContainText("Audífonos");


});


//Buscar Categorias de productos por medio de menú
test('TC_UI_004', async ({ page }) => {

  await page.goto('https://www.cyberpuerta.mx/');
  await expect(page).toHaveTitle(/Cyberpuerta.mx: Hardware, Computadoras, Laptops & Más/);

  const SelectCategory = page.locator("a[href='/Computo-Hardware/'][class='has-sub-categories'] ");
  await expect(SelectCategory).toBeVisible();
  await SelectCategory.click();


  const SelectSubCategory = page.locator("a[href='/Computo-Hardware/PC-Gaming/'][title='PC Gaming']");
  await expect(SelectSubCategory).toBeVisible();
  await SelectSubCategory.click();


  const SelectArticles = page.locator("a[href='https://www.cyberpuerta.mx/Tarjetas-de-Video-Gamer/'][class='subcat-content']");
  await expect(SelectArticles).toBeVisible();
  await SelectArticles.click();

  await expect(page.locator("h1")).toContainText("Tarjetas de Video Gamer");


});


//Agregar Producto a carrito
test('TC_UI_005', async ({ page }) => {

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

  const SelectCategory = page.locator("a[href='/Computo-Hardware/'][class='has-sub-categories'] ");
  await expect(SelectCategory).toBeVisible();
  await SelectCategory.click();


  const SelectSubCategory = page.locator("a[href='/Computo-Hardware/Componentes/'][title='Componentes']");
  await expect(SelectSubCategory).toBeVisible();
  await SelectSubCategory.click();

  const SelectArticles = page.locator("a[href='https://www.cyberpuerta.mx/Computo-Hardware/Componentes/Tarjetas-Madre/'][class='subcat-content']");
  await expect(SelectArticles).toBeVisible();
  await SelectArticles.click();

  await expect(page.locator("h1")).toContainText("Tarjetas Madre");


  const WatchArticle = page.locator("a[id='productList-2'][href='https://www.cyberpuerta.mx/Computo-Hardware/Componentes/Tarjetas-Madre/Tarjeta-Madre-Gigabyte-Micro-ATX-A520M-K-V2-S-AM4-AMD-A520-HDMI-64GB-DDR4-para-AMD.html']");
  await expect(WatchArticle).toBeVisible();
  await WatchArticle.click();

  await expect(page.locator("h1[class='detailsInfo_right_title']")).toContainText("Tarjeta Madre Gigabyte Micro-ATX A520M K V2, S-AM4, AMD A520, HDMI, 64GB DDR4 para AMD ");

  await page.waitForTimeout(1000);
  const AddToCart = page.locator("button[data-pre-process-add-to-cart='b6dc1c63a50bbd1fec4c93c3e96014ab']");
  await expect(AddToCart).toBeVisible();
  await AddToCart.click();


  const WatchcCart = page.locator("a[class='oxwidget_headerminibasket_header'][href='https://www.cyberpuerta.mx/carrito-de-compras/']");
  await expect(WatchcCart).toBeVisible();
  await WatchcCart.click();


  await expect(page.locator("div.emtitle a[href='https://www.cyberpuerta.mx/Computo-Hardware/Componentes/Tarjetas-Madre/Tarjeta-Madre-Gigabyte-Micro-ATX-A520M-K-V2-S-AM4-AMD-A520-HDMI-64GB-DDR4-para-AMD.html']")).toContainText("Tarjeta Madre Gigabyte Micro-ATX A520M K V2, S-AM4, AMD A520, HDMI, 64GB DDR4 para AMD");

  await expect(page.locator("div[class='basketboxcount']")).toContainText("Tienes 1 producto(s) en tu carrito");


  //await page.pause();


});




































