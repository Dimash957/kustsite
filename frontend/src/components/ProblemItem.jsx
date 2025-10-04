export default function ProblemItem({ item }) {
  const title = item?.title || 'Issue'
  const description = item?.description || ''
  const group = item?.group
  const categories = Array.isArray(item?.categories) ? item.categories.filter(Boolean) : []

  return (
    <li className="problem-item">
      <article>
        <h3 className="problem-title">{title}</h3>
        {description && <p className="problem-desc">{description}</p>}
        <div className="problem-meta">
          {group && <span className="chip" aria-label="User group">{group}</span>}
          {categories.length > 0 && (
            <ul className="chip-list" aria-label="Categories">
              {categories.map((cat) => (
                <li key={cat} className="chip">{cat}</li>
              ))}
            </ul>
          )}
        </div>
      </article>
    </li>
  )
}