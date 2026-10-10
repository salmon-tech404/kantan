/**
 * Kantanda — lớp cưỡng chế T1 bằng ESLint (flat config).
 *
 * Dùng: import và spread vào eslint.config.mjs của dự án, truyền tham số.
 *
 *   import kantanda from "../../10-kantanda/_system/tooling/eslint.config.mjs";
 *   export default [
 *     ...kantanda({ maxFnLines: 40, maxDepth: 3, ownershipKey: "userId" }),
 *     ...ruleRiengCuaDuAn,
 *   ];
 *
 * Mỗi rule ghi rõ ID Kantanda để khi lint báo lỗi thì tra được nguồn.
 * Chỉ chứa rule T1 — thứ máy bắt được với sai số gần 0.
 */

/** @param {{maxFnLines?:number, maxDepth?:number, srcDir?:string, domainDir?:string, infraDirs?:string[]}} p */
export default function kantanda(p = {}) {
  const maxFnLines = p.maxFnLines ?? 40;
  const maxDepth = p.maxDepth ?? 3;
  const domainDir = p.domainDir ?? "src/domain";
  const infraDirs = p.infraDirs ?? ["**/infrastructure/**", "**/prisma/**", "**/adapters/**"];

  return [
    {
      name: "kantanda/common",
      files: ["**/*.{ts,tsx,js,jsx}"],
      rules: {
        // CODE-FUN-002 — kích thước hàm và độ lồng
        "max-lines-per-function": ["error", { max: maxFnLines, skipBlankLines: true, skipComments: true }],
        "max-depth": ["error", maxDepth],
        // FE-TS-001 — zero any
        "@typescript-eslint/no-explicit-any": "error",
        // BE-ERR-002 — không rò stack trace ra response
        "no-restricted-syntax": [
          "error",
          {
            selector:
              "CallExpression[callee.property.name=/^(json|send)$/] MemberExpression[property.name='stack']",
            message: "BE-ERR-002: không đưa stack trace vào response. Dùng AppError với message an toàn.",
          },
          {
            selector: "NewExpression[callee.name='Error']:has(Identifier[name=/^(res|response)$/])",
            message: "BE-ERR-001: dùng AppError thay cho Error trần ở tầng HTTP.",
          },
        ],
      },
    },

    {
      name: "kantanda/backend-validation",
      files: ["**/*.ts"],
      ignores: ["**/*.test.ts", "**/*.spec.ts"],
      rules: {
        "no-restricted-syntax": [
          "error",
          {
            // BE-VAL-002 — z.object phải .strict() hoặc .strip() ở ranh giới request
            selector:
              "CallExpression[callee.object.name='z'][callee.property.name='object']:not(:has(~ MemberExpression[property.name=/^(strict|strip|passthrough)$/]))",
            message:
              "BE-VAL-002: schema ở ranh giới request phải .strict() (hoặc .strip() có chủ đích) để chặn mass assignment.",
          },
        ],
      },
    },

    {
      name: "kantanda/frontend",
      files: ["**/*.tsx"],
      rules: {
        "no-restricted-syntax": [
          "error",
          {
            // FE-API-001 — không gọi fetch/axios trực tiếp trong component
            selector:
              "JSXElement CallExpression[callee.name='fetch'], JSXElement CallExpression[callee.object.name='axios']",
            message: "FE-API-001: bọc lời gọi mạng trong hàm service có kiểu, không gọi thẳng trong JSX.",
          },
          {
            // UI-GEN-001 — không dùng emoji làm icon
            selector:
              "JSXText[value=/[\\u{1F300}-\\u{1FAFF}\\u{2600}-\\u{27BF}]/u]",
            message: "UI-GEN-001: dùng icon SVG (Lucide), không dùng emoji làm phần tử giao diện.",
          },
        ],
      },
    },

    {
      name: "kantanda/boundaries",
      files: [`${domainDir}/**/*.ts`],
      rules: {
        // ARCH-DDD-005 — domain không được phụ thuộc hạ tầng
        "no-restricted-imports": [
          "error",
          {
            patterns: [
              { group: infraDirs, message: "ARCH-DDD-005: domain không import hạ tầng. Định nghĩa port, để hạ tầng implement." },
              { group: ["@prisma/client", "axios", "express"], message: "ARCH-DDD-005: domain không phụ thuộc thư viện hạ tầng." },
            ],
          },
        ],
      },
    },

    {
      name: "kantanda/modularity",
      files: ["**/*.{ts,tsx}"],
      rules: {
        // ARCH-MOD-002 — không thò tay vào ruột module khác
        "no-restricted-imports": [
          "error",
          {
            patterns: [
              {
                group: ["**/features/*/internal/**", "**/modules/*/internal/**", "**/*/src/**"],
                message: "ARCH-MOD-002: chỉ import qua public interface của module, không đi vào đường dẫn nội bộ.",
              },
            ],
          },
        ],
      },
    },

    {
      name: "kantanda/testing",
      files: ["**/*.{test,spec}.{ts,tsx}"],
      rules: {
        "no-restricted-syntax": [
          "error",
          {
            // TEST-MCK-001 — chỉ mock dependency ngoài tiến trình
            selector: "CallExpression[callee.property.name='mock'] Literal[value=/^(\\.|~|@\\/)/]",
            message: "TEST-MCK-001: chỉ mock dependency ngoài tiến trình mà bạn không sở hữu. Không mock class/helper nội bộ.",
          },
          {
            // TEST-ANT-001 — không đếm số lần gọi nội bộ
            selector: "CallExpression[callee.property.name='toHaveBeenCalledTimes']",
            message: "TEST-ANT-001 / TEST-MCK-002: kiểm tra state và output, không kiểm tra số lần gọi phương thức nội bộ.",
          },
        ],
      },
    },
  ];
}
