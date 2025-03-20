Feature: OpenCart Automation
    Scenario: Agregar y luego eliminar un iPhone del cart
        Given Me encuentro en el HomePage de OpenCart http://www.opencart.abstracta.us/
        When Busco un "iPhone" en el search box
        And Selecciono el primer resultado
        And Agrego el producto al carrito
        And Abro el carrito
        Then Debería ver el "iPhone" seleccionado en el carrito
        And Elimino el producto del carrito 
        Then El "iPhone" ya no debería estar en el carrito
