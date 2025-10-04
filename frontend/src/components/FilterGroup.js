import React from 'react';
import '../styles/FilterGroup.css';

/**
 * FilterGroup Component
 * Accessible radio button group with fieldset and legend for screen readers
 */
function FilterGroup({ label, id, options, value, onChange, disabled = false }) {
  const handleChange = (e) => {
    if (!disabled) {
      onChange(e.target.value);
    }
  };

  return (
    <fieldset className="filter-group" disabled={disabled}>
      <legend className="filter-legend">{label}</legend>
      
      <div className="filter-options" role="radiogroup" aria-labelledby={`${id}-legend`}>
        {options.map((option) => {
          const optionId = `${id}-${option.replace(/\s+/g, '-').toLowerCase()}`;
          
          return (
            <div key={option} className="filter-option">
              <input
                type="radio"
                id={optionId}
                name={id}
                value={option}
                checked={value === option}
                onChange={handleChange}
                disabled={disabled}
                className="filter-radio"
              />
              <label 
                htmlFor={optionId} 
                className="filter-label"
              >
                {option}
              </label>
            </div>
          );
        })}
      </div>
    </fieldset>
  );
}

export default FilterGroup;
