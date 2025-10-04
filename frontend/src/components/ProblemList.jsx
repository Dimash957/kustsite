import ProblemItem from './ProblemItem'
import { useEffect, useRef } from 'react'

export default function ProblemList({ items = [], isLoading = false, error = '' }) {
  const liveRef = useRef(null)
  useEffect(() => {
    if (liveRef.current) {
      liveRef.current.textContent = isLoading ? 'Loading results…' : `${items.length} results`
    }
  }, [items.length, isLoading])

  return (
    <section aria-labelledby="results-heading" className="results-section">
      <h2 id="results-heading">Results</h2>
      <div ref={liveRef} aria-live="polite" aria-atomic="true" className="visually-hidden"></div>
      {error && <div role="alert" className="error">{error}</div>}
      <ul id="results" className="problem-list">
        {items.map((item, index) => (
          <ProblemItem key={index} item={item} />
        ))}
      </ul>
    </section>
  )
}