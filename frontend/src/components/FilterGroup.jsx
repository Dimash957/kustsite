export default function FilterGroup({ label, options = [], value, onChange, name }) {
  const groupName = name || label.replace(/\s+/g, '-').toLowerCase()
  return (
    <fieldset className="filter-group">
      <legend className="filter-legend">{label}</legend>
      <div className="filter-options">
        {options.map((option) => {
          const id = `${groupName}-${option.replace(/\s+/g, '-').toLowerCase()}`
          return (
            <div key={id} className="filter-option">
              <input
                type="radio"
                id={id}
                name={groupName}
                value={option}
                checked={value === option}
                onChange={() => onChange(option)}
              />
              <label htmlFor={id}>{option}</label>
            </div>
          )
        })}
      </div>
    </fieldset>
  )
}