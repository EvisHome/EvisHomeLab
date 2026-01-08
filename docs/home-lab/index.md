<style>
  .card {
    border: 1px solid #e1e1e1;
    border-radius: 8px;
    transition: 0.3s;
    padding: 0rem;
    background-color: #222;
  }
  .card:hover {
    background-color: #333;
  }
</style>

# Home Lab

Articles about my Home Lab.

## Highlights




<div class="grid cards" borderless style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; padding: 0px;">

  <div class="card">
    <p><a href="articles/ai-log-summary">
    <img src="articles/ai-log-summary/thumb.jpg" alt="CCTV" style="width:100%; border-radius: 8px;">
    <div style="padding: 0px 10px 10px 10px;">
      <h3>AI Log Summary </h3>
      <p>Turning log noise into actionable insights using AI.</p>
    </div>
    </a></p>
  </div>

  <div class="card">
    <p><a href="articles/dns-adguard-unbound">
    <img src="articles/dns-adguard-unbound/thumb.jpg" alt="Coffee" style="width:100%; border-radius: 8px; padding: 0px; margin: 0px;">
    <div style="padding: 0px 10px 10px 10px;">
      <h3>DNS: AdGuard Home & Unbound</h3>
      <p>Eliminating reliance on third parties. Coupling AdGuard Home (The Network Shield) with Unbound (The Recursive Resolver).</p>
    </div>
    </a></p>
  </div>

  <div class="card">
    <p><a href="articles/dns-adguard-unbound">
    <img src="https://via.placeholder.com/400x200?text=Connectivity" alt="Network" style="width:100%; border-radius: 8px;">
    <div style="padding: 0px 10px 10px 10px;">
      <h3>📡 Infrastructure</h3>
      <p>How our 🛰️ satellite dish keeps the house 🔊 speakers and smart devices online.</p>
    </div>
    </a></p>
  </div>

</div>

## Articles
{{ list_articles_grid() }}
