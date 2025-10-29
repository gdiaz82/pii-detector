TEST_CASES = [
    {
        'id': 1,
        'text': 'El cliente Juan Pérez con RUT 12.345.678-9 y email juan@empresa.com solicita información.',
        'expected_pii': {
            'email': ['juan@empresa.com'],
            'rut': ['12.345.678-9']
        }
    },
    {
        'id': 2, 
        'text': 'Contactar al teléfono +56 9 8765 4321 para confirmar la dirección en Av. Libertador 123.',
        'expected_pii': {
            'phone': ['+56 9 8765 4321']
        }
    },
    {
        'id': 3,
        'text': 'Texto normal sin información personal relevante para el negocio.',
        'expected_pii': {}
    },
    {
        'id': 4,
        'text': 'Tarjeta de crédito: 1234-5678-9012-3456 expira en 12/25',
        'expected_pii': {
            'credit_card': ['1234-5678-9012-3456']
        }
    },
    {
        'id': 5,
        'text': 'Múltiples emails: personal@gmail.com, trabajo@company.cl y spam@test.org',
        'expected_pii': {
            'email': ['personal@gmail.com', 'trabajo@company.cl', 'spam@test.org']
        }
    },
    {
        'id': 6,
        'text': 'RUT sin puntos: 12345678-9 y con puntos: 98.765.432-K',
        'expected_pii': {
            'rut': ['12345678-9', '98.765.432-K']
        }
    },
    {
        'id': 7,
        'text': 'Teléfonos variados: +1 (555) 123-4567, 56 2 2345 6789, 9-8765-4321',
        'expected_pii': {
            'phone': ['+1 (555) 123-4567', '56 2 2345 6789', '9-8765-4321']
        }
    },
    {
        'id': 9,
        'text': 'Email complejo: nombre.apellido+tag@subdominio.empresa.com.cl',
        'expected_pii': {
            'email': ['nombre.apellido+tag@subdominio.empresa.com.cl']
        }
    },
    {
        'id': 10,
        'text': 'Tarjeta con espacios: 1234 5678 9012 3456 y sin formato: 1234567890123456',
        'expected_pii': {
            'credit_card': ['1234 5678 9012 3456', '1234567890123456']
        }
    }
]