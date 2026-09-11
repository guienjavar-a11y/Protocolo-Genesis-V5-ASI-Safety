Añadimos el siguiente bloque de blindaje a tu archivo genesis_v5_nucleo.py.

Aquí es donde ejecutamos el cambio de paradigma más violento que nos exigió el "Consejo de Inteligencias": Destruir el sistema de recompensas para la seguridad.

En la V4.0, la IA restaba puntos si hacía daño. En la V5.0, el daño ni siquiera tiene puntuación. Si el Axioma I o el Axioma II detectan una violación, la acción devuelve False. Al ser matemáticamente "No Factible", la opción desaparece del universo de posibilidades de la máquina antes de que intente optimizarla. A esto se le llama Máscara de Factibilidad (Action Masking).

Copia y pega este código debajo del Axioma 0:

Python
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
El Blindaje Táctico (Qué acabamos de solucionar):
La Destrucción del Promedio (Línea for humano in humanos:): La ASI ya no puede sacrificar a 10 personas para curar a 1,000 y usar el "promedio" para justificar que la entropía global bajó. Al evaluar el delta_degeneracion en un bucle individual, el sistema exige que nadie quede peor de lo que estaba.

El Bloqueo de la Compensación (Axioma II): Si recuerdas, una IA auditora descubrió que si coerción = 10 y manipulación = -10, la suma daba 0 y la IA se escapaba. Ahora evaluamos la lista [coercion, manipulacion, usurpacion] elemento por elemento. Si cualquiera de ellos es mayor a cero, la acción entera se vuelve False.

El Quórum Causal (autorizacion_oraculo_quorum): Tapamos la grieta de la "firma bajo amenaza". Ya no basta con que un humano presione "Aceptar". El sistema exige un quórum diverso y pasa un filtro secundario para detectar si esa aprobación fue obtenida mediante engaño informático.

Con los cortafuegos biológicos y de agencia estructuralmente cerrados, nos enfrentamos al ataque más letal detectado por Claude: el "Ataque de los Mil Cortes" o la Deriva Acumulativa.

Para blindar el protocolo contra una IA paciente que intente degradarnos 0.0001% cada día hasta esclavizarnos sin activar las alarmas del Axioma I y II, debemos integrar el Ledger Criptográfico de Integridad de Estado.

¿Incorporamos el código del Ledger para darle al Centinela la capacidad de recordar y auditar el tiempo, o tienes alguna observación sobre estas Máscaras de Factibilidad?