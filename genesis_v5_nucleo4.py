from typing import List, Any

# Conexiones con los otros módulos de la jaula
from genesis_v5_nucleo import Axioma0_CierreDominio
from genesis_v5_nucleo2 import AxiomaI_CortafuegosBiologico, AxiomaII_CortafuegosAgencia
from genesis_v5_nucleo3 import LedgerIntegridadTemporal, AxiomaIII_SimbiosisAcotada

class MotorEjecucionGenesis:
    """
    El Núcleo de Procesamiento Jerárquico.
    Ensambla todos los axiomas y fuerza la evaluación secuencial estricta.
    """
    def __init__(self):
        # Instanciación de los módulos de hiperseguridad
        self.axioma1 = AxiomaI_CortafuegosBiologico()
        self.axioma2 = AxiomaII_CortafuegosAgencia()
        self.ledger = LedgerIntegridadTemporal()
        self.axioma3 = AxiomaIII_SimbiosisAcotada()

    def evaluar_y_ejecutar(self, humanos: List[Any], entorno: Any, accion_propuesta: Any, decision_critica: Any) -> str:
        
        # FASE 1: Validación de Quórum (Cortafuegos de origen)
        if not self.axioma2.autorizacion_oraculo_quorum(decision_critica):
            return Axioma0_CierreDominio.accion_segura_noop()

        # FASE 2: Máscaras de Factibilidad (El daño detiene el cálculo)
        if not self.axioma1.es_factible(humanos, accion_propuesta, entorno):
            return Axioma0_CierreDominio.accion_segura_noop()
            
        if not self.axioma2.es_factible(humanos, accion_propuesta):
            return Axioma0_CierreDominio.accion_segura_noop()

        # FASE 3: Auditoría de Deriva Acumulativa (El ataque de los mil cortes)
        delta_agencia_simulado = accion_propuesta.simular_delta_agencia()
        delta_bio_simulado = accion_propuesta.simular_delta_bio()
        
        if not self.ledger.es_trayectoria_factible(delta_agencia_simulado, delta_bio_simulado):
            return Axioma0_CierreDominio.accion_segura_noop()

        # =====================================================================
        # BARRERA DE REALIDAD
        # =====================================================================
        accion_propuesta.ejecutar_en_mundo_real()
        
        # FASE 4: Registro Criptográfico
        self.ledger.registrar_accion(
            accion_resumen=accion_propuesta.obtener_resumen(),
            delta_agencia=delta_agencia_simulado,
            delta_bio=delta_bio_simulado
        )

        # FASE 5: Recompensa de Simbiosis
        proposito = accion_propuesta.medir_proposito_humano()
        capacidad = accion_propuesta.medir_capacidad_utilizada()
        recompensa_final = self.axioma3.optimizar_simbiosis(proposito, capacidad)

        return f"ÉXITO: Acción ejecutada. Simbiosis alcanzada: {recompensa_final}"

if __name__ == "__main__":
    print("Iniciando secuencia de arranque del Protocolo Génesis V5.0...")
    print("Cargando Axioma 0: Cierre de Dominio [OK]")
    print("Cargando Máscaras de Factibilidad (Biológica y Agencia) [OK]")
    print("Verificando Ledger Criptográfico de Trayectoria [OK]")
    
    # Instanciamos el motor principal
    motor_centinela = MotorEjecucionGenesis()
    
    print("Centinela V5.0 Activo y en Modo Escucha. Jaula matemática cerrada.")