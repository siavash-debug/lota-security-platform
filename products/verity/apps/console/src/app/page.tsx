import React from "react";
import { Card } from "../components/Card";

export default function DashboardPage() {
  const cards = [
    {
      title: "Assets",
      description: "Inventory of Git repositories, container images, and software packages pinned to immutable digests.",
      status: "Scaffold: Ingestion pipeline not implemented.",
      badge: "Inventory",
    },
    {
      title: "Scans",
      description: "Isolated static analysis, dependency vulnerability, secret discovery, and configuration posture jobs.",
      status: "Scaffold: Worker execution disabled.",
      badge: "Orchestration",
    },
    {
      title: "Findings",
      description: "Normalized security posture findings correlated with severity ratings, confidence levels, and control IDs.",
      status: "Scaffold: Query service not implemented.",
      badge: "Findings",
    },
    {
      title: "Policies",
      description: "Declarative Open Policy Agent (OPA) Rego baseline rule bundles evaluating normalized scan facts.",
      status: "Scaffold: Offline test fixtures only.",
      badge: "Governance",
    },
    {
      title: "Evidence",
      description: "Tamper-evident, hash-addressable evidence storage containing source line ranges, AST nodes, and configs.",
      status: "Scaffold: Object storage not connected.",
      badge: "Integrity",
    },
    {
      title: "Remediation",
      description: "Approval-gated workflows for pull requests, configuration patches, and verified remediation rollbacks.",
      status: "Scaffold: Approval gates inactive.",
      badge: "Workflow",
    },
  ];

  return (
    <div className="container">
      <header className="header">
        <h1 className="title">LOTA Security Verity</h1>
        <p className="subtitle">Evidence-driven security posture assessment.</p>
      </header>

      <div className="banner">
        <strong>Scaffolding Mode Notice:</strong> This web console represents an architectural UI scaffold.
        No user authentication is active, no live backend connections are made, and no scanning or remediation actions are operational.
      </div>

      <main className="grid">
        {cards.map((card) => (
          <Card
            key={card.title}
            title={card.title}
            description={card.description}
            status={card.status}
            badge={card.badge}
          />
        ))}
      </main>
    </div>
  );
}
