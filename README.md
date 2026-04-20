# Entre Mujeres Legal — Backend API

## Pasos para desplegarlo en Vercel (15 minutos)

---

### PASO 1 — Obtén tu API Key de Anthropic

1. Ve a https://console.anthropic.com
2. Crea una cuenta (o inicia sesión)
3. Ve a "API Keys" → "Create Key"
4. Copia la key (empieza con `sk-ant-...`)
5. Guárdala en un lugar seguro — solo se muestra una vez

---

### PASO 2 — Sube el proyecto a GitHub

1. Ve a https://github.com y crea una cuenta si no tienes
2. Crea un repositorio nuevo llamado `entremujeres-backend`
3. Sube estos archivos:
   - `api/chat.js`
   - `vercel.json`
   - `package.json`

(Puedes arrastrar los archivos directo en GitHub, sin usar terminal)

---

### PASO 3 — Despliega en Vercel

1. Ve a https://vercel.com y crea una cuenta con tu GitHub
2. Clic en "Add New Project"
3. Selecciona tu repositorio `entremujeres-backend`
4. Clic en "Deploy" (sin cambiar nada)

---

### PASO 4 — Agrega tu API Key como variable de entorno

1. En tu proyecto de Vercel, ve a "Settings" → "Environment Variables"
2. Agrega:
   - **Name:** `ANTHROPIC_API_KEY`
   - **Value:** tu key `sk-ant-...`
3. Clic en "Save"
4. Ve a "Deployments" → clic en los tres puntos → "Redeploy"

---

### PASO 5 — Prueba que funciona

Vercel te dará una URL como:
`https://entremujeres-backend.vercel.app`

Tu endpoint de chat quedará en:
`https://entremujeres-backend.vercel.app/api/chat`

Pruébalo con este comando en la terminal (o usa Postman):

```bash
curl -X POST https://entremujeres-backend.vercel.app/api/chat \
  -H "Content-Type: application/json" \
  -d '{"messages":[{"role":"user","content":"Hola, necesito ayuda"}]}'
```

Deberías recibir una respuesta de la asesora jurídica.

---

### PASO 6 — Conecta tu frontend

En tu app React (el archivo gnjuridico.jsx), cambia la URL del fetch:

```js
// ANTES (no funciona en producción):
fetch("https://api.anthropic.com/v1/messages", ...)

// DESPUÉS (tu backend seguro):
fetch("https://entremujeres-backend.vercel.app/api/chat", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ messages })
})
```

---

## Costos estimados

| Uso mensual     | Costo aprox. |
|-----------------|--------------|
| 100 consultas   | $0.10 USD    |
| 1,000 consultas | $1.00 USD    |
| 5,000 consultas | $5.00 USD    |

*Usando Claude Haiku, el modelo más económico.*

---

## Seguridad incluida

- ✅ API Key nunca expuesta al usuario
- ✅ Máximo 20 mensajes por conversación
- ✅ Solo acepta método POST
- ✅ CORS configurado

---

¿Dudas? Pide ayuda en el chat de Entre Mujeres Legal.
