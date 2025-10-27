TEST_CASES = [
    {
        'id': 1,
        'text': 'El cliente Juan Pérez con RUT 12.345.678-9 y email juan@empresa.com solicita información.',
        'expected_pii': ['email', 'rut']
    },
    {
        'id': 2, 
        'text': 'Contactar al teléfono +56 9 8765 4321 para confirmar la dirección en Av. Libertador 123.',
        'expected_pii': ['phone', 'address']
    },
    {
        'id': 3,
        'text': 'Texto normal sin información personal relevante para el negocio.',
        'expected_pii': []
    }
]