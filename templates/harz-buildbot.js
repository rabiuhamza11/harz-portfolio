export default function handler(req, res) {
  const { method, body, query } = req;
  
  const projectTypes = {
    residential: { name: 'Residential Building', rate: 45000 },
    commercial: { name: 'Commercial Building', rate: 65000 },
    school: { name: 'School Building', rate: 55000 },
    mosque: { name: 'Mosque', rate: 50000 },
    warehouse: { name: 'Warehouse', rate: 35000 },
    renovation: { name: 'Renovation', rate: 15000 }
  };
  
  const cities = {
    abuja: 1.2, lagos: 1.15, kano: 0.9, kaduna: 0.85,
    ibadan: 0.95, port_harcourt: 1.1, enugu: 0.85, maiduguri: 0.8, jos: 0.9
  };
  
  if (method === 'GET') {
    return res.status(200).json({
      service: 'BuildBot AI',
      version: '2.0',
      endpoints: ['GET / (info)', 'POST /estimate', 'POST /materials'],
      projectTypes: Object.keys(projectTypes),
      cities: Object.keys(cities)
    });
  }
  
  if (method === 'POST' && body.action === 'estimate') {
    const { type, city, area, floors } = body;
    if (!projectTypes[type] || !cities[city]) {
      return res.status(400).json({ error: 'Invalid project type or city' });
    }
    const baseCost = projectTypes[type].rate * (area || 100) * (floors || 1);
    const cityMultiplier = cities[city];
    const total = Math.round(baseCost * cityMultiplier);
    const materials = Math.round(total * 0.55);
    const labor = Math.round(total * 0.30);
    const other = Math.round(total * 0.15);
    return res.status(200).json({
      project: projectTypes[type].name,
      city, area: area || 100, floors: floors || 1,
      breakdown: { materials, labor, other, total },
      timeline: `${Math.ceil((area || 100) / 50 * (floors || 1))} weeks`,
      currency: 'NGN'
    });
  }
  
  if (method === 'POST' && body.action === 'materials') {
    return res.status(200).json({
      materials: [
        { item: 'Cement (bags)', qty: 150, unitCost: 7500, total: 1125000 },
        { item: 'Sand (tons)', qty: 20, unitCost: 25000, total: 500000 },
        { item: 'Gravel (tons)', qty: 15, unitCost: 30000, total: 450000 },
        { item: 'Steel rods (tons)', qty: 3, unitCost: 850000, total: 2550000 },
        { item: 'Blocks (units)', qty: 2000, unitCost: 350, total: 700000 }
      ],
      totalCost: 5325000
    });
  }
  
  res.status(405).json({ error: 'Method not allowed' });
}
