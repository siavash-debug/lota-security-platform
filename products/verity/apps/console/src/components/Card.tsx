import React from "react";
import { DashboardCardProps } from "../lib/types";

export const Card: React.FC<DashboardCardProps> = ({
  title,
  description,
  status,
  badge = "Scaffold",
}) => {
  return (
    <div className="card">
      <div className="card-header">
        <h3 className="card-title">{title}</h3>
        <span className="card-badge">{badge}</span>
      </div>
      <p className="card-desc">{description}</p>
      <div className="card-status">{status}</div>
    </div>
  );
};
