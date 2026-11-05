import typer
import json
from rich.console import Console
from rich.panel import Panel
from vision_agent.agent import VisionWorkforceAgent

app = typer.Typer(help="Saudi Vision 2030 Workforce & SDG Alignment Agent CLI")
console = Console()


@app.command()
def analyze(enterprise_id: str = typer.Option("COMP-101", help="Target Enterprise ID to evaluate")):
    """Run workforce alignment and Nitaqat compliance analysis for an enterprise."""
    console.print(Panel.fit("[bold cyan]Initializing Saudi Vision 2030 Workforce Agent...[/bold cyan]"))
    
    agent = VisionWorkforceAgent(mode="mock")
    report = agent.run_workflow(enterprise_id=enterprise_id)
    
    console.print(json.dumps(report, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    app()
