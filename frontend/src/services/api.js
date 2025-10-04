const BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:5000'

export async function analyzeText(text, group, category) {
  const payload = { text, group, category }
  const response = await fetch(`${BASE_URL}/analyze`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  })

  if (!response.ok) {
    // Try to parse error JSON; fallback to status text
    let detail = ''
    try {
      const data = await response.json()
      detail = data?.error || ''
    } catch {}
    throw new Error(detail || `Request failed: ${response.status}`)
  }

  const data = await response.json()
  const issues = Array.isArray(data?.issues) ? data.issues : []
  // Normalize strings to objects for rendering consistency
  return issues.map((issue) =>
    typeof issue === 'string'
      ? { title: issue, description: issue, group, categories: category ? [category] : [] }
      : issue,
  )
}
