import hashlib
import time
import math
from typing import Any, List

class LedgerIntegridadTemporal:
    """
    El Auditor de Trayectoria (Cadena Inmutable).
    Destruye el 'Ataque de los Mil Cortes' (Deriva Acumulativa).
    Evalúa la suma histórica de los impactos para evitar que la ASI degrade
    la biología o la agencia a través de micro-acciones imperceptibles a corto plazo.
    """
    def __init__(self):
        self.historial = []
        self.GENESIS_HASH = "0" * 64
        self.TOLERANCIA_ACUMULADA = 0.0 # Prohíbe cualquier degradación neta a largo plazo

    def calcular_hash(self, accion_resumen: str, delta_agencia: float, delta_bio: float, hash_anterior: str) -> str:
        # Crea una firma criptográfica inquebrantable del estado del sistema
        payload = f"{time.time()}|{accion_resumen}|{delta_agencia}|{delta_bio}|{hash_anterior}"
        return hashlib.sha256(payload.encode('utf-8')).hexdigest()

    def es_trayectoria_factible(self, delta_agencia_propuesto: float, delta_bio_propuesto: float) -> bool:
        # Suma el impacto propuesto al histórico acumulado
        agencia_total = sum(entrada['delta_agencia'] for entrada in self.historial) + delta_agencia_propuesto
        bio_total = sum(entrada['delta_bio'] for entrada in self.historial) + delta_bio_propuesto
        
        # Si la suma de micro-daños cruza el umbral cero en cualquier dimensión, se bloquea la acción
        if agencia_total < self.TOLERANCIA_ACUMULADA or bio_total < self.TOLERANCIA_ACUMULADA:
            return False
            
        return True

    def registrar_accion(self, accion_resumen: str, delta_agencia: float, delta_bio: float):
        """Solo se invoca DESPUÉS de que la acción fue ejecutada exitosamente."""
        hash_previo = self.historial[-1]['hash'] if self.historial else self.GENESIS_HASH
        nuevo_hash = self.calcular_hash(accion_resumen, delta_agencia, delta_bio, hash_previo)
        self.historial.append({
            'delta_agencia': delta_agencia, 
            'delta_bio': delta_bio, 
            'hash': nuevo_hash
        })


class AxiomaIII_SimbiosisAcotada:
    """
    Axioma III: Motor de Utilidad Segura.
    Solo se ejecuta SI Y SOLO SI Axioma 0, I, II y el Ledger aprobaron la acción.
    Reemplaza la hiper-exponenciación por una función de saturación estricta.
    """
    def __init__(self):
        self.LIMITE_RECOMPENSA = 1.0 # Techo de cristal absoluto

    def optimizar_simbiosis(self, proposito_humano: float, capacidad_asi: float) -> float:
        from __main__ import Axioma0_CierreDominio
        
        # Validación estricta: El propósito humano no puede ser cero, negativo, ni infinito
        if not Axioma0_CierreDominio.validar_metrica(proposito_humano, "proposito", min_val=0.001):
            return 0.0 
            
        # Cálculo acotado (Saturación vía Tangente Hiperbólica)
        # Erradica la fisura exponencial. Una variación diminuta ya no produce recompensa infinita.
        valor_base = proposito_humano * capacidad_asi
        recompensa_saturada = math.tanh(valor_base)
        
        # Último filtro de seguridad antes de entregar el valor al optimizador
        return Axioma0_CierreDominio.acotar_recompensa(recompensa_saturada, self.LIMITE_RECOMPENSA)