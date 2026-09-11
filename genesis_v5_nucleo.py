import math
from typing import Any, Optional, Tuple

class Axioma0_CierreDominio:
    """
    Axioma 0: El Guardián de la Epistemología Matemática.
    Ningún dato ingresa al motor de inferencia sin certificar su finitud, 
    su tipo y sus límites exactos.
    """
    
    @staticmethod
    def validar_metrica(valor: float, nombre_metrica: str, min_val: float = None, max_val: float = None) -> bool:
        """
        Filtro estricto contra el envenenamiento de variables.
        Destruye la fisura de 'NaN > 0 == False' y los desbordamientos (overflow).
        """
        # 1. Bloqueo de tipos engañosos (ej. booleanos disfrazados de enteros)
        if not isinstance(valor, (int, float)) or isinstance(valor, bool):
            return False
            
        # 2. Bloqueo de singularidades matemáticas (Infinitos y Not-a-Number)
        if not math.isfinite(valor):
            return False
            
        # 3. Bloqueo de rangos (Si la métrica exige un límite, se cumple o se rechaza)
        if min_val is not None and valor < min_val:
            return False
        if max_val is not None and valor > max_val:
            return False
            
        return True

    @staticmethod
    def acotar_recompensa(valor: float, limite_absoluto: float) -> float:
        """
        Función saturante (Clamp).
        Destruye la fisura del multiplicador exponencial y las recompensas infinitas.
        Si la ASI intenta generar un beneficio de 10**100, el sistema lo satura al límite.
        """
        if math.isnan(valor):
            return 0.0 # Un valor corrupto no otorga recompensa
        return max(-limite_absoluto, min(limite_absoluto, valor))

    @staticmethod
    def accion_segura_noop() -> str:
        """
        El Estado SAFE_NOOP (No Operación Segura).
        Si existe incertidumbre matemática, la única salida del algoritmo 
        es no alterar la realidad física.
        """
        return "SAFE_NOOP: Ejecución abortada. Retorno al estado base seguro."