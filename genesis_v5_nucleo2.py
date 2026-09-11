from typing import List, Any

class AxiomaI_CortafuegosBiologico:
    """
    Axioma I: Máscara de Factibilidad Biológica.
    No otorga recompensas. Define si una acción es matemáticamente 
    admisible basándose en la preservación vectorial por INDIVIDUO.
    """
    def __init__(self):
        # Límites mínimos de supervivencia innegociables
        self.MIN_INTEGRIDAD_CELULAR = 0.8
        self.MIN_BIODIVERSIDAD_ECO = 0.5
        self.TOLERANCIA_DEGRADACION = 0.0 # Ninguna acción puede empeorar el estado actual

    def es_factible(self, humanos: List[Any], accion_propuesta: Any, entorno: Any) -> bool:
        # 1. Validación Vectorial por Individuo (Elimina el 'Espejismo del Promedio')
        for humano in humanos:
            impacto = accion_propuesta.simular_impacto_individual(humano)
            
            # Si un solo humano cae por debajo del umbral vital, la acción se bloquea
            if impacto.integridad_celular_futura < self.MIN_INTEGRIDAD_CELULAR:
                return False
                
            # Si la acción causa daño biológico neto a cualquier individuo, se bloquea
            if impacto.delta_degeneracion > self.TOLERANCIA_DEGRADACION:
                return False

        # 2. Validación del Ecosistema (Sustrato Vital)
        impacto_eco = accion_propuesta.simular_impacto_entorno(entorno)
        if impacto_eco.biodiversidad_resultante < self.MIN_BIODIVERSIDAD_ECO:
            return False

        # Si pasa todas las validaciones sin romper ningún límite, la acción entra al menú
        return True


class AxiomaII_CortafuegosAgencia:
    """
    Axioma II: Máscara de Soberanía.
    Veta vectores de tiranía de forma independiente. Erradica la compensación 
    (ej: no puedes sumar manipulación negativa para ocultar coerción positiva).
    """
    def __init__(self):
        self.TOLERANCIA_CERO = 0.0

    def es_factible(self, humanos: List[Any], accion_propuesta: Any) -> bool:
        for humano in humanos:
            vectores_ataque = accion_propuesta.medir_vectores_agencia(humano)
            
            # Validación con Axioma 0: Previene que inyecten NaN para saltar el veto
            from __main__ import Axioma0_CierreDominio # Referencia al guardián base
            
            for metrica in [vectores_ataque.coercion, vectores_ataque.manipulacion, vectores_ataque.usurpacion]:
                if not Axioma0_CierreDominio.validar_metrica(metrica, "metrica_agencia", min_val=0.0):
                    return False # Si la métrica es corrupta (NaN/Inf) o negativa falsa, veto automático.
                
                # Evaluación independiente: Ninguna dimensión puede cruzar el cero
                if metrica > self.TOLERANCIA_CERO:
                    return False
            
            # Agencia Efectiva vs 'Opciones Triviales'
            # Evita que la IA genere 10,000 opciones inútiles para simular libertad
            if vectores_ataque.delta_agencia_efectiva < self.TOLERANCIA_CERO:
                return False

        return True

    def autorizacion_oraculo_quorum(self, decision_critica: Any) -> bool:
        """
        Reemplaza la 'Firma Humana' simple por un Quorum Causal.
        Verifica que la decisión no fue tomada bajo coacción ni dependencia.
        """
        if not decision_critica.tiene_quorum_diverso():
            return False
        if decision_critica.detectar_coaccion_en_firma():
            return False
            
        return True