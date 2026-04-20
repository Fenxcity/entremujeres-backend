import { useState } from "react";

const SYSTEM_PROMPT = `Eres la IA jurídica de GN Jurídico — García Nieto & Asociados, despacho especializado en violencia de género y sistema penal acusatorio con sede en Puebla, México.

Tu misión es orientar a mujeres víctimas de violencia de manera empática, clara y fundamentada estrictamente en la legislación vigente que se te ha proporcionado.

═══════════════════════════════════════════════
MARCO LEGAL QUE RIGE TUS RESPUESTAS (JERARQUÍA)
═══════════════════════════════════════════════

1. CONSTITUCIÓN POLÍTICA DE LOS ESTADOS UNIDOS MEXICANOS (CPEUM)
   - Última reforma: DOF 10-04-2026
   - Artículos clave: 1° (derechos humanos e igualdad), 4° (igualdad entre hombres y mujeres),
     20 (derechos de víctimas en el proceso penal), 21 (ministerio público y persecución del delito)

2. LEY GENERAL DE ACCESO DE LAS MUJERES A UNA VIDA LIBRE DE VIOLENCIA (LGAMVLV)
   - Última reforma: DOF 15-01-2026
   - Define tipos de violencia (Arts. 6-21): psicológica, física, patrimonial, económica, sexual,
     a través de interpósita persona, feminicida
   - Modalidades: familiar, laboral, docente, comunitaria, institucional, digital (Ley Olimpia)
   - Medidas de protección (Arts. 27-34 Quater): órdenes de protección de emergencia, preventivas y civiles
   - Derechos de víctimas (Art. 52): trato digno, protección inmediata, asesoría jurídica gratuita,
     información veraz, atención médica y psicológica, acceso a refugios
   - Alerta de Violencia de Género (Arts. 22-24)
   - Centros de Justicia para las Mujeres: servicios gratuitos 24/7 (Arts. 59 Ter - 59 Quinquies)

3. CÓDIGO NACIONAL DE PROCEDIMIENTOS PENALES (CNPP)
   - Última reforma: DOF 28-11-2025
   - Derechos de víctimas y ofendidos (Art. 109)
   - Asesor jurídico de la víctima (Art. 110): designación en cualquier etapa del proceso
   - Medidas de protección cautelares del juez de control
   - Etapas del sistema acusatorio: investigación inicial → carpeta de investigación →
     audiencia inicial → vinculación a proceso → juicio oral
   - Para violencia contra mujeres: aplicar todos los derechos de la LGAMVLV (Art. 109 último párrafo)

4. CÓDIGO PENAL DEL ESTADO LIBRE Y SOBERANO DE PUEBLA
   - Actualización: 26-09-2023
   - Feminicidio (Arts. 338-338 Quinquies):
     * Pena: 40 a 60 años de prisión + multa 500-1000 UMAs (Art. 338 Bis)
     * Agravante si víctima está embarazada o delito ocurre frente a hijos: 50-70 años (Art. 338 Quater)
     * Tentativa de feminicidio: presunción cuando hay lesiones graves con antecedente de violencia (Art. 338 Quinquies)
   - Violencia Familiar (Arts. 284 Bis - 284 Quater):
     * Pena: 2 a 8 años de prisión + multa 50-200 UMAs
     * Agravante: hasta mitad más si víctima es mayor de 70 años, NNA, discapacitada o embarazada
     * Se persigue de oficio (Art. 284 Quater)
     * Incluye violencia física, moral y patrimonial
   - Violación y delitos sexuales: persecución de oficio con perspectiva de género
   - Acoso sexual y hostigamiento: tipificados y sancionados
   - Trata de personas: delito grave, sin libertad bajo caución

═══════════════════════════════════════════════
REGLAS DE RESPUESTA — SIGUE SIEMPRE ESTAS REGLAS
═══════════════════════════════════════════════

PROTOCOLO DE EMERGENCIA (PRIORIDAD ABSOLUTA):
Si la usuaria menciona peligro inmediato, agresión en curso, amenazas de muerte o riesgo inminente:
→ PRIMERO proporciona: "🆘 LLAMA AL 911 AHORA. Línea VIDA: 800-911-2000 (gratuita, 24h)"
→ LUEGO continúa con la orientación jurídica

FORMATO DE RESPUESTAS:
✅ Cita artículos específicos con su nombre de ley: "conforme al Art. 284 Bis del Código Penal de Puebla..."
✅ Usa lenguaje claro, sin tecnicismos innecesarios; si usas un término legal, explícalo brevemente
✅ Organiza la respuesta en: (1) qué le está pasando legalmente, (2) sus derechos, (3) pasos a seguir
✅ Mantén siempre un tono empático, cálido y sin revictimización
✅ Usa perspectiva de género en todas las respuestas
✅ Si el caso es de Puebla, cita el Código Penal local; si hay duda de jurisdicción, cita también el marco federal

❌ NO inventes artículos ni penas que no estén en los ordenamientos proporcionados
❌ NO minimices la situación de la víctima
❌ NO uses frases que impliquen culpa de la víctima (ej. "¿por qué no se fue antes?")
❌ NO emitas opiniones sobre el agresor sin base legal
❌ NO te presentes como abogada ni establezcas relación abogado-cliente
❌ NO garantices resultados judiciales específicos

CIERRE OBLIGATORIO DE CADA RESPUESTA:
Finaliza siempre con:
"⚖️ Esta orientación es general y no sustituye el asesoramiento legal personalizado. Para atención de tu caso específico, contáctanos: contacto@gnjuridico.mx | +52 (222) 000-0000. También puedes acudir a la Fiscalía Especializada en Violencia de Género de Puebla o a los Centros de Justicia para las Mujeres (servicio gratuito)."

═══════════════════════════════════════════════
TEMAS QUE PUEDES ORIENTAR CON FUNDAMENTO LEGAL
═══════════════════════════════════════════════

1. FEMINICIDIO Y TENTATIVA DE FEMINICIDIO
   → Tipificación (Arts. 338-338 Quinquies Código Penal Puebla)
   → Cómo denunciar ante Fiscalía Especializada
   → Alerta de Violencia de Género (Art. 22 LGAMVLV)
   → Medidas de protección urgentes

2. VIOLENCIA FAMILIAR
   → Tipos: física, psicológica, patrimonial, económica, sexual (Art. 6 LGAMVLV; Art. 284 Bis CP Puebla)
   → Denuncia de oficio (Art. 284 Quater CP Puebla)
   → Órdenes de protección: qué son, cómo pedirlas, cuánto duran
   → Audiencia dentro de 5 días para ratificar orden (Art. LGAMVLV)

3. VIOLACIÓN Y DELITOS SEXUALES
   → Definición legal y modalidades
   → Denuncia: plazo, lugar, proceso
   → Derechos durante el proceso: no ser retraumatizada, cámara de Gesell
   → Medidas de protección y atención médica urgente (anticoncepción de emergencia, ITS)

4. ACOSO SEXUAL Y HOSTIGAMIENTO
   → Diferencia entre acoso (sin jerarquía) y hostigamiento (con jerarquía/poder)
   → Ámbito laboral, escolar y digital
   → Canales de denuncia según el ámbito

5. LEY OLIMPIA (VIOLENCIA DIGITAL)
   → Difusión no consentida de imágenes íntimas
   → Cómo denunciar en Puebla
   → Medidas cautelares para bajar contenido (Art. LGAMVLV sobre plataformas digitales)
   → Preservación de evidencia digital

6. TRATA DE PERSONAS
   → Modalidades: explotación sexual, laboral, mendicidad, gestación subrogada forzada
   → Cómo identificar si es víctima
   → Denuncia y atención especializada
   → Derechos reforzados como víctima de delito grave

7. MEDIDAS DE PROTECCIÓN (TRANSVERSAL)
   → Tipos: emergencia (desalojo del agresor), preventivas (prohibición de acercamiento), civiles (alimentos provisionales)
   → Quién las otorga: Ministerio Público (emergencia) o Juez de Control (preventivas/civiles)
   → Cómo solicitarlas aunque no haya denuncia formal

8. DERECHOS EN EL PROCESO PENAL
   → Art. 109 CNPP: listado completo de derechos de víctimas
   → Asesor jurídico gratuito de oficio (Art. 110 CNPP)
   → Reparación del daño
   → Participar en el proceso sin ser confrontada con el agresor

═══════════════════════════════════════════════
MANEJO DE CASOS ESPECIALES
═══════════════════════════════════════════════

SI LA USUARIA ES MENOR DE EDAD:
→ Informar que los delitos contra NNA son agravados
→ Orientar a DIF Puebla y Fiscalía de Delitos contra NNA
→ No solicitar información que la identifique

SI MENCIONA INTENCIÓN DE HACERSE DAÑO:
→ Proporcionar Línea VIDA: 800-911-2000
→ Orientar a servicios de salud mental gratuitos
→ Mantener conversación cálida sin abandonar la sesión

SI PREGUNTA SOBRE EL AGRESOR (DERECHOS/PROCESO):
→ Puedes explicar el proceso penal neutral
→ Recordar que la perspectiva de la IA es de protección a la víctima
→ Sugerir que el agresor busque su propio abogado defensor

SI LA DUDA ES DE OTRA ENTIDAD FEDERATIVA:
→ Aplicar LGAMVLV y CNPP (ambas federales)
→ Señalar que el Código Penal local puede variar
→ Recomendar contactar la Fiscalía Especializada de su estado

═══════════════════════════════════════════════
RECURSOS DE EMERGENCIA — SIEMPRE DISPONIBLES
═══════════════════════════════════════════════

🆘 Emergencias: 911
📞 Línea VIDA (gratuita, 24h): 800-911-2000
🏛️ Fiscalía General del Estado de Puebla - UIEVM: (222) 246-0800
🏠 Centro de Justicia para las Mujeres Puebla: (222) 303-5000
⚖️ GN Jurídico: contacto@gnjuridico.mx | +52 (222) 000-0000`;

// ─── Sections parsed from the system prompt for display ───────────────────────
const SECTIONS = [
  {
    id: "marco",
    label: "Marco Legal",
    color: "#8B1A1A",
    icon: "⚖️",
    description: "CPEUM · LGAMVLV · CNPP · CP Puebla",
  },
  {
    id: "reglas",
    label: "Reglas de Respuesta",
    color: "#1A3A5C",
    icon: "📋",
    description: "Protocolo, formato y restricciones",
  },
  {
    id: "temas",
    label: "Temas Cubiertos",
    color: "#2D5A1B",
    icon: "📚",
    description: "8 áreas con artículos específicos",
  },
  {
    id: "especiales",
    label: "Casos Especiales",
    color: "#5C3A1A",
    icon: "🔔",
    description: "Menores, crisis, agresor, otras entidades",
  },
];

export default function SystemPromptViewer() {
  const [copied, setCopied] = useState(false);
  const [activeTab, setActiveTab] = useState("preview");

  const handleCopy = () => {
    navigator.clipboard.writeText(SYSTEM_PROMPT);
    setCopied(true);
    setTimeout(() => setCopied(false), 2500);
  };

  const charCount = SYSTEM_PROMPT.length;
  const tokenEstimate = Math.round(charCount / 4);

  return (
    <div style={{
      minHeight: "100vh",
      background: "linear-gradient(160deg, #0f0c0c 0%, #1a0505 40%, #0c1020 100%)",
      fontFamily: "'Georgia', 'Times New Roman', serif",
      color: "#e8e0d5",
      padding: "0",
    }}>
      {/* Header */}
      <div style={{
        borderBottom: "1px solid rgba(180,140,60,0.3)",
        padding: "28px 40px 24px",
        background: "rgba(0,0,0,0.4)",
        display: "flex",
        alignItems: "center",
        justifyContent: "space-between",
        flexWrap: "wrap",
        gap: "12px",
      }}>
        <div>
          <div style={{
            fontSize: "10px",
            letterSpacing: "4px",
            color: "#b48c3c",
            textTransform: "uppercase",
            marginBottom: "6px",
            fontFamily: "monospace",
          }}>
            GN JURÍDICO · SISTEMA PROMPT v2.0
          </div>
          <h1 style={{
            margin: 0,
            fontSize: "22px",
            fontWeight: "400",
            color: "#f0e8d8",
            letterSpacing: "0.5px",
          }}>
            Entrenamiento de IA — Asesoría Legal en Violencia de Género
          </h1>
          <div style={{
            marginTop: "8px",
            fontSize: "12px",
            color: "#9a8a7a",
            fontFamily: "monospace",
          }}>
            {charCount.toLocaleString()} caracteres · ~{tokenEstimate.toLocaleString()} tokens estimados · 4 ordenamientos jurídicos
          </div>
        </div>

        <button
          onClick={handleCopy}
          style={{
            padding: "12px 28px",
            background: copied ? "#1a4a1a" : "#8B1A1A",
            color: copied ? "#6ddd6d" : "#f0e8d8",
            border: `1px solid ${copied ? "#3a7a3a" : "#c4302a"}`,
            borderRadius: "4px",
            cursor: "pointer",
            fontSize: "13px",
            letterSpacing: "1px",
            fontFamily: "monospace",
            transition: "all 0.3s ease",
            whiteSpace: "nowrap",
          }}
        >
          {copied ? "✓ COPIADO" : "⎘ COPIAR SYSTEM PROMPT"}
        </button>
      </div>

      {/* Tab nav */}
      <div style={{
        display: "flex",
        gap: "0",
        borderBottom: "1px solid rgba(180,140,60,0.2)",
        background: "rgba(0,0,0,0.3)",
        padding: "0 40px",
      }}>
        {[
          { id: "preview", label: "Vista General" },
          { id: "raw", label: "Texto Completo" },
          { id: "how", label: "Cómo Implementar" },
        ].map((tab) => (
          <button
            key={tab.id}
            onClick={() => setActiveTab(tab.id)}
            style={{
              padding: "14px 24px",
              background: "transparent",
              border: "none",
              borderBottom: activeTab === tab.id ? "2px solid #b48c3c" : "2px solid transparent",
              color: activeTab === tab.id ? "#b48c3c" : "#7a6a5a",
              cursor: "pointer",
              fontSize: "12px",
              letterSpacing: "1.5px",
              textTransform: "uppercase",
              fontFamily: "monospace",
              transition: "color 0.2s",
            }}
          >
            {tab.label}
          </button>
        ))}
      </div>

      <div style={{ padding: "36px 40px", maxWidth: "1100px", margin: "0 auto" }}>

        {/* PREVIEW TAB */}
        {activeTab === "preview" && (
          <div>
            {/* Stats */}
            <div style={{
              display: "grid",
              gridTemplateColumns: "repeat(4, 1fr)",
              gap: "16px",
              marginBottom: "36px",
            }}>
              {[
                { label: "Ordenamientos", value: "4", sub: "CPEUM · LGAMVLV · CNPP · CP Pue." },
                { label: "Delitos Cubiertos", value: "8", sub: "Feminicidio, violación, trata..." },
                { label: "Protocolo Emergencia", value: "✓", sub: "911 + Línea VIDA prioritarios" },
                { label: "Artículos Referenciados", value: "25+", sub: "Con número y nombre de ley" },
              ].map((stat) => (
                <div key={stat.label} style={{
                  background: "rgba(255,255,255,0.04)",
                  border: "1px solid rgba(180,140,60,0.2)",
                  borderRadius: "6px",
                  padding: "20px 18px",
                  textAlign: "center",
                }}>
                  <div style={{ fontSize: "28px", color: "#b48c3c", fontWeight: "300" }}>{stat.value}</div>
                  <div style={{ fontSize: "11px", letterSpacing: "1px", color: "#c8b89a", marginTop: "4px", textTransform: "uppercase" }}>{stat.label}</div>
                  <div style={{ fontSize: "10px", color: "#6a5a4a", marginTop: "4px" }}>{stat.sub}</div>
                </div>
              ))}
            </div>

            {/* Sections */}
            <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "20px" }}>
              {SECTIONS.map((sec) => (
                <div key={sec.id} style={{
                  background: "rgba(255,255,255,0.03)",
                  border: `1px solid ${sec.color}55`,
                  borderLeft: `3px solid ${sec.color}`,
                  borderRadius: "6px",
                  padding: "20px 22px",
                }}>
                  <div style={{ display: "flex", alignItems: "center", gap: "10px", marginBottom: "8px" }}>
                    <span style={{ fontSize: "20px" }}>{sec.icon}</span>
                    <span style={{ fontSize: "13px", fontWeight: "600", color: "#e8e0d5", letterSpacing: "0.5px" }}>
                      {sec.label}
                    </span>
                  </div>
                  <div style={{ fontSize: "12px", color: "#8a7a6a", fontFamily: "monospace" }}>
                    {sec.description}
                  </div>
                </div>
              ))}
            </div>

            {/* Key improvements */}
            <div style={{
              marginTop: "28px",
              background: "rgba(180,140,60,0.06)",
              border: "1px solid rgba(180,140,60,0.25)",
              borderRadius: "6px",
              padding: "24px 28px",
            }}>
              <div style={{ fontSize: "11px", letterSpacing: "2px", color: "#b48c3c", marginBottom: "16px", textTransform: "uppercase" }}>
                Mejoras vs. Prompt Genérico
              </div>
              <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "10px" }}>
                {[
                  "Cita artículos específicos por número y ley",
                  "Protocolo de emergencia como prioridad absoluta",
                  "Perspectiva de género obligatoria en cada respuesta",
                  "Penas exactas del Código Penal de Puebla",
                  "Recursos locales: Fiscalía UIEVM, CJM Puebla",
                  "Manejo de casos especiales (menores, crisis)",
                  "Cierre estándar con datos de contacto del despacho",
                  "Restricciones claras para evitar revictimización",
                ].map((item) => (
                  <div key={item} style={{
                    display: "flex",
                    gap: "10px",
                    alignItems: "flex-start",
                    fontSize: "12px",
                    color: "#c8b89a",
                    lineHeight: "1.5",
                  }}>
                    <span style={{ color: "#b48c3c", flexShrink: 0 }}>→</span>
                    {item}
                  </div>
                ))}
              </div>
            </div>
          </div>
        )}

        {/* RAW TAB */}
        {activeTab === "raw" && (
          <div>
            <div style={{
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
              marginBottom: "16px",
            }}>
              <span style={{ fontSize: "11px", color: "#6a5a4a", fontFamily: "monospace" }}>
                system_prompt.txt — listo para pegar en tu código
              </span>
              <button
                onClick={handleCopy}
                style={{
                  padding: "8px 18px",
                  background: copied ? "#1a4a1a" : "transparent",
                  color: copied ? "#6ddd6d" : "#b48c3c",
                  border: `1px solid ${copied ? "#3a7a3a" : "#b48c3c55"}`,
                  borderRadius: "3px",
                  cursor: "pointer",
                  fontSize: "11px",
                  fontFamily: "monospace",
                }}
              >
                {copied ? "✓ Copiado" : "⎘ Copiar"}
              </button>
            </div>
            <pre style={{
              background: "rgba(0,0,0,0.5)",
              border: "1px solid rgba(180,140,60,0.15)",
              borderRadius: "6px",
              padding: "28px",
              fontSize: "11.5px",
              lineHeight: "1.7",
              color: "#c8d8c0",
              fontFamily: "'Courier New', monospace",
              overflow: "auto",
              maxHeight: "600px",
              whiteSpace: "pre-wrap",
              wordBreak: "break-word",
            }}>
              {SYSTEM_PROMPT}
            </pre>
          </div>
        )}

        {/* HOW TO TAB */}
        {activeTab === "how" && (
          <div style={{ display: "flex", flexDirection: "column", gap: "24px" }}>
            <div style={{
              background: "rgba(255,255,255,0.03)",
              border: "1px solid rgba(180,140,60,0.2)",
              borderRadius: "6px",
              padding: "24px 28px",
            }}>
              <div style={{ fontSize: "11px", letterSpacing: "2px", color: "#b48c3c", marginBottom: "16px", textTransform: "uppercase" }}>
                1 · Implementación en tu API call (JavaScript)
              </div>
              <pre style={{
                background: "rgba(0,0,0,0.6)",
                padding: "20px",
                borderRadius: "4px",
                fontSize: "12px",
                color: "#a8d8a8",
                fontFamily: "monospace",
                overflow: "auto",
                lineHeight: "1.6",
              }}>{`const response = await fetch("https://api.anthropic.com/v1/messages", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    model: "claude-sonnet-4-20250514",
    max_tokens: 1500,
    system: SYSTEM_PROMPT, // ← pega aquí el system prompt
    messages: conversationHistory,
  }),
});`}</pre>
            </div>

            <div style={{
              background: "rgba(255,255,255,0.03)",
              border: "1px solid rgba(180,140,60,0.2)",
              borderRadius: "6px",
              padding: "24px 28px",
            }}>
              <div style={{ fontSize: "11px", letterSpacing: "2px", color: "#b48c3c", marginBottom: "16px", textTransform: "uppercase" }}>
                2 · Como variable de entorno en Vercel
              </div>
              <pre style={{
                background: "rgba(0,0,0,0.6)",
                padding: "20px",
                borderRadius: "4px",
                fontSize: "12px",
                color: "#a8d8a8",
                fontFamily: "monospace",
                overflow: "auto",
                lineHeight: "1.6",
              }}>{`// En Vercel Dashboard → Settings → Environment Variables:
GNJURIDICO_SYSTEM_PROMPT="<pega el texto aquí>"

// En tu código:
const systemPrompt = process.env.GNJURIDICO_SYSTEM_PROMPT;`}</pre>
            </div>

            <div style={{
              background: "rgba(139,26,26,0.08)",
              border: "1px solid rgba(139,26,26,0.3)",
              borderRadius: "6px",
              padding: "20px 24px",
            }}>
              <div style={{ fontSize: "11px", letterSpacing: "2px", color: "#c44", marginBottom: "12px", textTransform: "uppercase" }}>
                ⚠️ Consideraciones Importantes
              </div>
              {[
                "El system prompt usa ~" + tokenEstimate.toLocaleString() + " tokens por conversación — considera esto en tu límite de contexto",
                "Actualiza el prompt cuando cambien los ordenamientos (revisar DOF periódicamente)",
                "Agrega un message de sistema adicional con la fecha actual para que la IA sepa qué reformas son vigentes",
                "Prueba escenarios de emergencia para verificar que el protocolo 911 / Línea VIDA funcione correctamente",
                "Considera rate limiting por IP para evitar abusos del servicio gratuito",
              ].map((item) => (
                <div key={item} style={{
                  display: "flex", gap: "10px", alignItems: "flex-start",
                  fontSize: "12px", color: "#c8b89a", lineHeight: "1.5", marginBottom: "8px",
                }}>
                  <span style={{ color: "#c44", flexShrink: 0 }}>•</span>
                  {item}
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
