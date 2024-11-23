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


//Agregar Producto a carrito(Cambiar de forma de busqueda para buscar este prodcuto en al barra de busqueda  ASUS Laptop Gamer ASUS TUF Gaming F15 FX507VV)
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

  const InputArticle = page.locator("input[name='searchparam'][placeholder='¿Qué producto buscas el día de hoy?']");
  await expect(InputArticle).toBeVisible();
  await InputArticle.fill(" ASUS Laptop Gamer ASUS TUF Gaming F15 FX507VV");
  await page.keyboard.press('Enter');


  const WatchArticle = page.locator("a[id='searchList-1'][href='https://www.cyberpuerta.mx/Computadoras/Laptops/Laptop-Gamer-ASUS-TUF-Gaming-F15-FX507VV-15-6-1920x1080-Full-HD-Intel-Core-i7-13620H-NVIDIA-GeForce-RTX-4060-16GB-1TB-SSD-Windows-11-Home-Espanol.html']");
  await expect(WatchArticle).toBeVisible();
  await WatchArticle.click();

  await expect(page.locator("a[title='FX507VV-LP313W']")).toContainText("FX507VV-LP313W");

  await page.waitForTimeout(1000);
  const AddToCart = page.locator("button[data-pre-process-add-to-cart='2121a373323021e2d130c4ab1b2e53d0']");
  await expect(AddToCart).toBeVisible();
  await AddToCart.click();


  const ClearWindow = page.locator("i[class='cpx-icon cpx-icon--primary c-popup-2__close-btn']");
  await expect(ClearWindow).toBeVisible();
  await ClearWindow.click();


  const WatchcCart = page.locator("a[class='oxwidget_headerminibasket_header'][href='https://www.cyberpuerta.mx/carrito-de-compras/']");
  await expect(WatchcCart).toBeVisible();
  await WatchcCart.click();


  await expect(page.locator("div.emtitle a[href='https://www.cyberpuerta.mx/Computadoras/Laptops/Laptop-Gamer-ASUS-TUF-Gaming-F15-FX507VV-15-6-1920x1080-Full-HD-Intel-Core-i7-13620H-NVIDIA-GeForce-RTX-4060-16GB-1TB-SSD-Windows-11-Home-Espanol.html']")).toBeVisible();

  await expect(page.locator("div[class='basketboxcount']")).toContainText("Tienes 1 producto(s) en tu carrito");


 // await page.pause();


});




































