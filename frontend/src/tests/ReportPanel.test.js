import React from "react";
import { render, screen, fireEvent, waitFor } from "@testing-library/react";
import ReportPanel from "../components/ReportPanel";
import * as api from "../utils/api";

// Mock the downloadReport function
jest.mock("../utils/api", () => ({
  downloadReport: jest.fn(),
}));

describe("ReportPanel", () => {
  beforeEach(() => {
    api.downloadReport.mockResolvedValue();
  });

  it("renders and calls downloadReport on click", async () => {
    render(<ReportPanel region="hurricane_gulf" />);
    const button = screen.getByRole("button", { name: /Generate Report/i });
    expect(button).toBeInTheDocument();

    fireEvent.click(button);
    expect(button).toBeDisabled();

    await waitFor(() => {
      expect(api.downloadReport).toHaveBeenCalledWith("hurricane_gulf");
      // Button should return to enabled state
      expect(button).not.toBeDisabled();
    });
  });
});
