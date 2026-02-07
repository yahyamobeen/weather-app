const form = document.getElementById('city-form');
const input = document.getElementById('city-input');
const status = document.getElementById('status');
const result = document.getElementById('result');

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  const city = input.value.trim();
  if (!city) return;
  status.textContent = 'Loading...';
  result.classList.add('hidden');
  try {
    const resp = await fetch('/weather', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ city })
    });
    if (!resp.ok) {
      const errText = await resp.text();
      status.textContent = `Server error: ${resp.status} ${errText}`;
      return;
    }
    const data = await resp.json();
    console.log('weather response', data);
    status.textContent = '';
    // Try multiple keys/paths for temperature
    let temp = null;
    if (data) {
      if (typeof data.temperature !== 'undefined') temp = data.temperature;
      else if (typeof data.temp !== 'undefined') temp = data.temp;
      else if (data.current && typeof data.current.temp_c !== 'undefined') temp = data.current.temp_c;
      else if (data.current && typeof data.current.temp !== 'undefined') temp = data.current.temp;
      else if (data.data && typeof data.data.temperature !== 'undefined') temp = data.data.temperature;
    }
    // Show only temperature; if not found, display a simple message (don't show full JSON)
    if (temp !== null && typeof temp !== 'undefined') {
      result.textContent = `${temp} °C`;
    } else {
      result.textContent = 'Temperature not available';
      console.warn('Temperature not found in response; response object:', data);
    }
    result.classList.remove('hidden');
  } catch (err) {
    status.textContent = 'Network error: ' + err.message;
  }
});
