import { useEffect, useMemo, useState } from "react";
import { apiRequest } from "../lib/api.js";

function LineChart({ chart, activeSeries, setActiveSeries }) {
  const width = 620;
  const height = 280;
  const padding = 36;
  const allValues = chart.series.flatMap((series) => series.values);
  const max = Math.max(...allValues);
  const min = Math.min(...allValues);
  const range = Math.max(1, max - min);

  function pointFor(index, value) {
    const x = padding + (index * (width - padding * 2)) / (chart.xLabels.length - 1);
    const y = height - padding - ((value - min) / range) * (height - padding * 2);
    return `${x},${y}`;
  }

  return (
    <div className="insight-graph-shell">
      <svg viewBox={`0 0 ${width} ${height}`} className="insight-svg" role="img">
        <rect x="0" y="0" width={width} height={height} rx="26" className="chart-surface" />
        {[0, 1, 2, 3].map((step) => {
          const y = padding + (step * (height - padding * 2)) / 3;
          return <line key={step} x1={padding} y1={y} x2={width - padding} y2={y} className="chart-grid-line" />;
        })}
        {chart.series.map((series) => {
          const points = series.values.map((value, index) => pointFor(index, value)).join(" ");
          const isActive = activeSeries === series.name;
          return (
            <g key={series.name}>
              <polyline
                points={points}
                fill="none"
                stroke={series.color}
                strokeWidth={isActive ? 5 : 3}
                strokeOpacity={isActive ? 1 : 0.45}
              />
              {series.values.map((value, index) => {
                const [x, y] = pointFor(index, value).split(",");
                return (
                  <circle
                    key={`${series.name}-${chart.xLabels[index]}`}
                    cx={x}
                    cy={y}
                    r={isActive ? 6 : 4}
                    fill={series.color}
                    fillOpacity={isActive ? 1 : 0.75}
                  />
                );
              })}
            </g>
          );
        })}
        {chart.xLabels.map((label, index) => {
          const x = padding + (index * (width - padding * 2)) / (chart.xLabels.length - 1);
          return (
            <text key={label} x={x} y={height - 10} textAnchor="middle" className="chart-axis-label">
              {label}
            </text>
          );
        })}
      </svg>
      <div className="chart-legend-tabs">
        {chart.series.map((series) => (
          <button
            key={series.name}
            className={activeSeries === series.name ? "legend-chip active" : "legend-chip"}
            onClick={() => setActiveSeries(series.name)}
            type="button"
          >
            <span className="swatch" style={{ background: series.color }} />
            {series.name}
          </button>
        ))}
      </div>
    </div>
  );
}

function ScatterChart({ chart, selectedPoint, setSelectedPoint }) {
  const width = 620;
  const height = 280;
  const padding = 40;
  const maxX = Math.max(...chart.points.map((point) => point.x));
  const minX = Math.min(...chart.points.map((point) => point.x));
  const maxY = Math.max(...chart.points.map((point) => point.y));
  const minY = Math.min(...chart.points.map((point) => point.y));

  function scaledX(value) {
    return padding + ((value - minX) / (maxX - minX)) * (width - padding * 2);
  }

  function scaledY(value) {
    return height - padding - ((value - minY) / (maxY - minY)) * (height - padding * 2);
  }

  return (
    <div className="insight-graph-shell">
      <svg viewBox={`0 0 ${width} ${height}`} className="insight-svg" role="img">
        <rect x="0" y="0" width={width} height={height} rx="26" className="chart-surface" />
        <line x1={padding} y1={height - padding} x2={width - padding} y2={height - padding} className="chart-grid-line strong" />
        <line x1={padding} y1={padding} x2={padding} y2={height - padding} className="chart-grid-line strong" />
        <line
          x1={scaledX(minX)}
          y1={scaledY(maxY - 6)}
          x2={scaledX(maxX)}
          y2={scaledY(minY + 6)}
          className="trend-line"
        />
        {chart.points.map((point) => {
          const active = selectedPoint?.label === point.label;
          return (
            <g key={point.label}>
              <circle
                cx={scaledX(point.x)}
                cy={scaledY(point.y)}
                r={active ? 11 : 8}
                className={active ? "scatter-point active" : "scatter-point"}
                onMouseEnter={() => setSelectedPoint(point)}
              />
              <text x={scaledX(point.x)} y={scaledY(point.y) - 16} textAnchor="middle" className="chart-axis-label">
                {point.label}
              </text>
            </g>
          );
        })}
        <text x={width / 2} y={height - 8} textAnchor="middle" className="chart-axis-label">
          {chart.xLabel}
        </text>
        <text x="16" y={height / 2} textAnchor="middle" className="chart-axis-label chart-axis-vertical">
          {chart.yLabel}
        </text>
      </svg>
      <div className="scatter-readout">
        <strong>{selectedPoint.label}</strong>
        <span>Work intensity: {selectedPoint.x}</span>
        <span>Consumption index: {selectedPoint.y}</span>
        <p>{selectedPoint.region} cluster observation from the prior analysis story.</p>
      </div>
    </div>
  );
}

function BarChart({ chart, highlightedBar, setHighlightedBar }) {
  const max = Math.max(...chart.bars.map((bar) => bar.value));

  return (
    <div className="bar-chart">
      {chart.bars.map((bar) => {
        const active = highlightedBar === bar.label;
        return (
          <button
            key={bar.label}
            className={active ? "bar-row active" : "bar-row"}
            onMouseEnter={() => setHighlightedBar(bar.label)}
            onClick={() => setHighlightedBar(bar.label)}
            type="button"
          >
            <span className="bar-label">{bar.label}</span>
            <div className="bar-track">
              <div
                className="bar-fill"
                style={{
                  width: `${(bar.value / max) * 100}%`,
                  background: bar.color
                }}
              />
            </div>
            <strong>{bar.value}</strong>
          </button>
        );
      })}
    </div>
  );
}

export function InsightsPage() {
  const [insights, setInsights] = useState([]);
  const [dashboard, setDashboard] = useState(null);
  const [activeChart, setActiveChart] = useState("consumption-trend");
  const [activeSeries, setActiveSeries] = useState("High income");
  const [selectedPoint, setSelectedPoint] = useState(null);
  const [highlightedBar, setHighlightedBar] = useState("Cultural norms");

  useEffect(() => {
    apiRequest("/api/insights").then((data) => {
      setInsights(data.insights);
      setDashboard(data.dashboard);
      setSelectedPoint(data.dashboard.charts.find((item) => item.id === "work-vs-consumption")?.points[0] || null);
    });
  }, []);

  const chart = useMemo(
    () => dashboard?.charts.find((entry) => entry.id === activeChart) || null,
    [activeChart, dashboard]
  );

  if (!dashboard || !chart) {
    return (
      <section className="panel">
        <p className="eyebrow">Did You Know?</p>
        <h2>Loading the coffee storyboards...</h2>
      </section>
    );
  }

  return (
    <div className="insights-layout">
      <section className="panel insights-hero">
        <div>
          <p className="eyebrow">Did You Know?</p>
          <h2>Interactive coffee insight gallery</h2>
          <p className="lead">{dashboard.headline}</p>
        </div>
        <div className="insight-metric-grid">
          {dashboard.spotlightMetrics.map((metric) => (
            <article key={metric.label} className="insight-metric-card">
              <span>{metric.label}</span>
              <strong>{metric.value}</strong>
              <p>{metric.detail}</p>
            </article>
          ))}
        </div>
      </section>

      <section className="panel">
        <div className="panel-header">
          <div>
            <p className="eyebrow">Insight Lab</p>
            <h2>Read the analysis as graphs, not just text</h2>
          </div>
          <div className="chart-tabs">
            {dashboard.charts.map((entry) => (
              <button
                key={entry.id}
                className={activeChart === entry.id ? "legend-chip active" : "legend-chip"}
                onClick={() => setActiveChart(entry.id)}
                type="button"
              >
                {entry.title}
              </button>
            ))}
          </div>
        </div>
        <p className="lead">{chart.narrative}</p>
        {chart.type === "line" ? (
          <LineChart chart={chart} activeSeries={activeSeries} setActiveSeries={setActiveSeries} />
        ) : null}
        {chart.type === "scatter" && selectedPoint ? (
          <ScatterChart chart={chart} selectedPoint={selectedPoint} setSelectedPoint={setSelectedPoint} />
        ) : null}
        {chart.type === "bar" ? (
          <BarChart chart={chart} highlightedBar={highlightedBar} setHighlightedBar={setHighlightedBar} />
        ) : null}
      </section>

      <div className="page-grid">
        <section className="panel">
          <p className="eyebrow">Interpretation Cards</p>
          <h2>Short takeaways from the original analysis</h2>
          <div className="insight-grid">
            {insights.map((insight) => (
              <article key={insight.id} className="insight-card story-card">
                <h3>{insight.title}</h3>
                <p>{insight.body}</p>
              </article>
            ))}
          </div>
        </section>

        <section className="panel">
          <p className="eyebrow">Coffee History</p>
          <h2>How coffee became a lifestyle signal</h2>
          <div className="timeline">
            {dashboard.timeline.map((item) => (
              <article key={item.era} className="timeline-card">
                <span className="timeline-era">{item.era}</span>
                <strong>{item.title}</strong>
                <small>{item.period}</small>
                <p>{item.body}</p>
              </article>
            ))}
          </div>
        </section>
      </div>

      <section className="panel insight-footnote">
        <p className="eyebrow">Boundary</p>
        <h2>Insights inform the story, not the drink choice</h2>
        <p>
          This section visualizes the prior analysis and broader coffee context for discovery and
          learning. Recommendation logic remains intentionally separate so the app does not confuse
          macro-level insight with individual taste matching.
        </p>
      </section>
    </div>
  );
}
